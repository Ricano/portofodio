from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse
from django.utils import timezone

from django.views.generic import TemplateView
from pytube import YouTube

from main.models import ContactForm, Project


class MainView(TemplateView):
    template_name = "main.html"

    extra_context = {
        "year": timezone.now().year,
        "game_url": "/static/html5/index.html",
        "form": ContactForm,
        "projects": Project.objects.all()
    }

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            send_mail(
                        'New message from your website, sent by ' + contact.email,
                        f'Email: {contact.email}\n\nMessage: {contact.message}',
                        'depoisdizcomofoi@hotmail.com',
                        ['depoisdizcomofoi@gmail.com'],
                        fail_silently=False,
                    )
            return HttpResponseRedirect("/")
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors})



class YoutubeView(TemplateView):
    template_name = "youtube.html"

    def post(self, request):
        link = request.POST.get("text")
        video = YouTube(link).streams.get_highest_resolution().download(".")
        return self.render_to_response({"link": video.title})
