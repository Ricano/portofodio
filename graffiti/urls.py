from django.urls import path

from graffiti.views import GraffitiView

urlpatterns = [
    path("", GraffitiView.as_view(), name="graffiti"),
]
