from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('home/',views.home,name="home"),
    path('educative/',views.educative,name="educative"),
    path('formulario/',views.searchform,name="formulario")
]
