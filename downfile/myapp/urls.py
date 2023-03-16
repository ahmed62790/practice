from django.urls import path
from . import views
from django.conf import settings
#from django_downloadview import  ObjectDownloadView
from django.conf.urls.static import static
from django import obj
from .models import files 


download = ObjectDownloadView.as_view(model = files, file_field= 'file')


urlpatterns = [
    path('', views.files, name='files'),
    path('download//', download, name="default"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)