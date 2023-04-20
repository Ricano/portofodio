import datetime

from django import forms
from django.db import models
from django.db.models import Choices
from django.utils import timezone


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Font(Choices):
    BASIC = "Roboto"
    CREEPY = "Creepster"
    VINYL = "Monoton"
    WILDWEST = "Rye"
    CIRCUS = "Henny Penny"
    GAMING = "Press Start 2P"
    LOVE = "Emilys Candy"
    SHADE3D = "Bungee Shade"
    GRAFFITI = "Another"
    MINIMALISTIC = "Gruppo"


class Graffiti(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    font = models.CharField(choices=Font.choices, max_length=30)
    text = models.CharField(max_length=64)
    location_x = models.IntegerField(default=0, null=True)
    location_y = models.IntegerField(default=0, null=True)
    color = models.CharField(max_length=7)
    created = models.DateField(default=timezone.now)
    rotation = models.IntegerField(default=0)

    def __str__(self):
        return f'"{self.text}" by {self.author.name}'

    def width(self):
        return 0


class GraffitiForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"cols": "30", "rows": "8", "placeholder": "Your message"}), label="",max_length=64)
    author = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your name"}), label="", max_length=30)
    font = forms.ChoiceField(choices=Font.choices, label="")
    location_x = forms.IntegerField(widget=forms.HiddenInput())
    location_y = forms.IntegerField(widget=forms.HiddenInput())
