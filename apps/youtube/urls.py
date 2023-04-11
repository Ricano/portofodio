from django.urls import path

from apps.youtube.views import YoutubeView, DownloadView

urlpatterns = [

    path("", YoutubeView.as_view(), name="youtube"),
    path("download", DownloadView.as_view(), name="download"),
]
