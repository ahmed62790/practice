from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20)
    region = models.CharField(max_length=2, choices=[('NA', 'North America')])
    moderator = models.BooleanField()

    def __str__(self):
        return self.name