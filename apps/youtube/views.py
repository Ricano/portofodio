import datetime

from django.shortcuts import render
from django.views import View
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
        form = YouTubeForm(request.POST)
        context = {"form": form}
        link = request.POST.get("link")
        if form.is_valid():
            try:
                yt = YouTube(link)
                stream_choices = []
                for stream in yt.fmt_streams:
                    if stream.type == "audio":
                        stream_choices.append([stream.mime_type, f"{stream.abr} - {stream.audio_codec}"])
                    else:
                        stream_choices.append([stream.mime_type, f"{stream.resolution} - {stream.video_codec}"])

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

class DownloadView(View):
    def post(self, request):
        form = DownloadForm(request.POST)
        audio_only = request.POST.get("audio_only")
        print(form)




