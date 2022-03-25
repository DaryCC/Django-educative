from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index,name="index"),
    path('home/',views.home,name="home"),
    path('educative/',views.educative,name="educative"),
    path('forms/',views.forms,name="form"),
]
