from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=200)
    store_url = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

# Create your models here.
