from django.contrib import admin

from apps.graffiti.models import Author, Graffiti

# Register your models here.
admin.site.register(Author)
admin.site.register(Graffiti)