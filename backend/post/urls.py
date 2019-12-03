from django.urls import path
from . import views

urlpatterns = [
    path('post/update/<int:post_pk>/', views.update),
    path('post/create/', views.create),
    path('post/', views.index),
]