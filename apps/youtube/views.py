import datetime

from django.http import JsonResponse
from django.shortcuts import render, redirect
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
                context["video"] = {
                    "title": yt.title,
                    "author": yt.author,
                    "length": str(datetime.timedelta(seconds=yt.length)),
                    "thumbnail_url": yt.thumbnail_url
                }
            except RegexMatchError:
                context["error"] = {
                    "link": '"' + link + '"',
                    "message": "does not appear to be a valid link"
                }
            except PytubeError as e:
                context["error"] = {
                    "link": e.__context__,
                    "message": "Pytube error"
                }
            except Exception as e:
                context["error"] = {
                    "link": e.__context__,
                    "message": "Unhandled exception error"
                }
        return render(request, "youtube.html", context=context)

class DownloadView(View):
    def post(self, request):
        form = DownloadForm(request.POST)
        audio_only = request.POST.get("audio_only")
        print(form)




