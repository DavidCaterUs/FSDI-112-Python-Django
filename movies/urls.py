from django.urls import path
from . import views

urlpatterns = [
    path('welcome', views.welcome, name="welcome"),
    path('myname', views.myname, name="myname"),
    path('hello', views.index, name="hello"),

]
