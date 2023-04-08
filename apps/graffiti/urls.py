from django.urls import path

from apps.graffiti.views import GraffitiView

urlpatterns = [
    path("", GraffitiView.as_view(), name="graffiti"),
]
