from django.db import models
from django import forms


class Project(models.Model):
    title = models.CharField(max_length=30)
    link = models.CharField(max_length=100)
    image_link = models.CharField(max_length=100)
    resume = models.CharField(max_length=100)
    description = models.CharField(max_length=360)

    def __str__(self):
        return self.title


class TechLink(models.Model):
    text = models.CharField(max_length=360)
    icon = models.CharField(max_length=30)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'message')
