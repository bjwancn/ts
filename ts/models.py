from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Stock(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
