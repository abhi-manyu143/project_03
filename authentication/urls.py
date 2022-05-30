from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name= "login"),
    path('login', views.dashboard, name= "dashboard"),
    path('signout', views.signout, name = "signout"),
    
]