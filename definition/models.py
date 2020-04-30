from django.db import models
from django.urls import reverse 

# Create your models here.
class Definition (models.Model):
    title       = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse("definitions:definition-detail", kwargs={"id": self.id})