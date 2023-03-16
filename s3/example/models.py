
from django.db import models

# Create your models here.


class file(models.Model):
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to='media/')