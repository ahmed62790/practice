from django.db import models

# Create your models here.
class files(models.Model):
    file = models.FileField(upload_to= 'my_files/',blank = True)
    file_title = models.CharField(max_length=200)