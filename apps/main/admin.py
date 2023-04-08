from django.contrib import admin

from apps.main.models import TechLink, Project, Contact

# Register your models here.
admin.site.register(TechLink)
admin.site.register(Project)
admin.site.register(Contact)