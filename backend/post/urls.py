from django.urls import path
from . import views

urlpatterns = [
    path('post/delete/<int:post_pk>/', views.delete_post),
    path('post/update/<int:post_pk>/', views.update_post),
    path('post/<int:post_pk>/', views.read_post),
    path('post/create/', views.create_post),
    path('post/', views.index),
]