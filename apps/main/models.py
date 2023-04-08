from django.db import models
from django import forms


class TechLink(models.Model):
    name = models.CharField(max_length=36)
    text = models.CharField(max_length=360)
    icon = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=30)
    link = models.CharField(max_length=100)
    image_link = models.CharField(max_length=100)
    resume = models.CharField(max_length=100)
    description = models.CharField(max_length=360)
    tech_links = models.ManyToManyField(TechLink)


    def __str__(self):
        return self.title




class Contact(models.Model):
    email = models.EmailField(verbose_name=" your email")
    message = models.TextField(verbose_name=" message", max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix
    class Meta:
        model = Contact
        fields = ('email', 'message')
