from django.urls import path
from .views import *
 
urlpatterns = [
    path('', home),
    path('example/', example),
    path('buble/', buble),
    path('new/', new),
    path('new2/', new2),
    path('new3/', new3),
    path('new4/', new4)

]