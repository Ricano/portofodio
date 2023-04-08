from django.db.transaction import atomic
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView

from apps.graffiti.models import Graffiti, GraffitiForm, Author



class GraffitiView(TemplateView):
    template_name = "graffiti.html"


    def get(self, request, *args, **kwargs):
        graffiti_list = Graffiti.objects.all()
        context = {"graffiti_list": graffiti_list, "form": GraffitiForm()}

        return self.render_to_response(context)


    @atomic
    def post(self, request):
        form = GraffitiForm(request.POST)
        if form.is_valid():
            author, _ = Author.objects.get_or_create(name=request.POST.get("author"))

            font = request.POST.get("font")
            text = request.POST.get("text")
            location_x = request.POST.get("location_x")
            location_y = request.POST.get("location_y")
            color = request.POST.get("color")
            rotation = request.POST.get("rotation")
            Graffiti.objects.create(author=author, font=font, text=text, location_x=location_x, location_y=location_y, color=color, rotation=rotation)
            return HttpResponseRedirect("/graffiti")
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors})

    # def delete(self, *args):
    #     Graffiti.objects.all().delete()
    #     return HttpResponseRedirect("/graffiti")

