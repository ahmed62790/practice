from django.contrib import admin

# Register your models here.
from.models import student

# Register your models here.
@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display = ['id', 'name','roll','city']