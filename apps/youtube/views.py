from django.views.generic import TemplateView
from pytube import YouTube




class YoutubeView(TemplateView):
    template_name = "youtube.html"

    def post(self, request):
        link = request.POST.get("text")
        video = YouTube(link).streams.get_highest_resolution().download(".")
        return self.render_to_response({"link": video.title})
