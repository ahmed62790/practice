from django.shortcuts import render
from.models import student

import datetime
# Create your views here.
def index(request):

    current_date = datetime.date.today()
    formated_date = current_date.strftime("%d-%b-%y")
    obj = student.objects.all()
    return render(request, 'index.html',
                  {
                    "obj" : obj,
                    'current_date': current_date,
                   'formated_date': formated_date
                   })
    



    