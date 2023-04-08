from django.urls import path

from apps.youtube.views import YoutubeView

urlpatterns = [

    path("", YoutubeView.as_view(), name="youtube"),
]
