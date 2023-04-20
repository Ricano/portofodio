from django.db import models
from django import forms


# Create your models here.

class YouTube(models.Model):
    link = models.CharField(max_length=360)
    title = models.CharField(max_length=360)


class YouTubeForm(forms.Form):
    link = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "place link here"}), label="", max_length=360, error_messages={
        "required": "missing link"})


class DownloadForm(forms.Form):
    stream = forms.CharField(required=False, label="", widget=forms.Select(choices=[]))
