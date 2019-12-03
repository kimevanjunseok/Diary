from django.urls import path
from . import views

urlpatterns = [
    path('post/update/<int:post_pk>/', views.update),
    path('post/<int:post_pk>/', views.read_post),
    path('post/create/', views.create),
    path('post/', views.index),
]