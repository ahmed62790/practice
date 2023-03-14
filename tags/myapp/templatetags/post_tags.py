from django import template
from ..models import student
import datetime

 

register = template.Library()


@register.simple_tag
def total_stud():
    return student.objects.count()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)