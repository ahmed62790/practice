from django.apps import AppConfig


class blogconfig(AppConfig):
    default_site = 'blog.admin.area'


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
