import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from pytube import YouTube
from pytube.exceptions import RegexMatchError, PytubeError

from apps.youtube.models import YouTubeForm, DownloadForm


class YoutubeView(TemplateView):
    template_name = "youtube.html"

    extra_context = {
        "form": YouTubeForm(),
        "form2": DownloadForm()
    }

    def post(self, request):
        if request.POST.get("link") is not None:
            form = YouTubeForm(request.POST)
            context = {"form": form}
            link = request.POST.get("link")
            if form.is_valid():
                try:
                    yt = YouTube(link)
                    request.session["link"] = link

                    # Sort by filesize. Make sure 'only audio' ones appear at the bottom
                    stream_choices = []
                    video_choices = []
                    audio_choices = []
                    for stream in yt.streams.order_by("filesize").__reversed__():
                        if stream.type == "audio":
                            audio_choices.append(
                                [stream.itag,
                                 f"Audio Only - {round(stream.filesize_mb, 2)}MB - {stream.abr} - {stream.mime_type.split('/')[1]} - {stream.audio_codec}"
                                 ]
                            )
                        elif stream.is_progressive:
                            stream_choices.append(
                                [stream.itag,
                                 f"{round(stream.filesize_mb, 2)}MB - {stream.resolution} - {stream.fps}fps - {stream.mime_type.split('/')[1]} - {stream.video_codec}"
                                 ]
                            )
                        else:
                            video_choices.append(
                                [stream.itag,
                                 f"Video Only -  {round(stream.filesize_mb, 2)}MB - {stream.resolution} - {stream.fps}fps - {stream.mime_type.split('/')[1]} - {stream.video_codec}"
                                 ]
                            )
                    stream_choices.extend(video_choices)
                    stream_choices.extend(audio_choices)

                    form2 = DownloadForm(request.POST)
                    form2.fields["stream"].widget.choices = stream_choices
                    context["form2"] = form2
                    context["video"] = {
                        "title": yt.title,
                        "author": yt.author,
                        "length": str(datetime.timedelta(seconds=yt.length)),
                        "thumbnail_url": yt.thumbnail_url
                    }
                except RegexMatchError:
                    context["error"] = {
                        "link": link,
                        "message": "does not appear to be a valid link"
                    }
                except PytubeError as e:
                    context["error"] = {
                        "link": e,
                        "message": "Pytube error"
                    }
                except Exception as e:
                    context["error"] = {
                        "link": e,
                        "message": "Unhandled exception error"
                    }

            return render(request, "youtube.html", context=context)
        else:
            form = DownloadForm(request.POST)

            stream = YouTube(request.session["link"]).streams.get_by_itag(form.data.get("stream"))
            stream.download()
            return render(request, "youtube_success.html")
