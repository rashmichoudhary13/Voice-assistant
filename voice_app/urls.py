from django.contrib import admin
from django.urls import path
from voice_app import views

# from .views import listen_to_voice

urlpatterns = [
    path("",views.index, name="index"),
    path('listen/', views.listen, name='listen'),
]