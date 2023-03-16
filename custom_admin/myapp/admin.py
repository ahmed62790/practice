from django.contrib import admin
from . import models
# Register your models here.

class myappadminarea(admin.AdminSite):
    site_header = 'myapp admin area'

blog_site = myappadminarea(name='myappadmin')
blog_site.register(models.post)
admin.site.register(models.post)