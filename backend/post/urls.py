from django.urls import path
from . import views

urlpatterns = [
    path('post/create/', views.create),
    path('post/', views.index),
]