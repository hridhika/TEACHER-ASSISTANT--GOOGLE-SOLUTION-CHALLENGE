from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.authorize,name='auth'),
    path('auth/',views.authorize,name='auth'),
    path('logout/',views.logout,name='logout'),
    path('usertype/',views.usertype,name='usertype'),
]