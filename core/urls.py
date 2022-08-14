from django.urls import path
from . import views

from django.conf import settings


urlpatterns = [
    path('', views.viewgetTopicos, name='getTopicos'),
    path('mural/', views.viewgetMural, name='getMural'),
    # path('getFile', views.getFile, name='getFile')
    
]