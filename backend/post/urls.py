from django.urls import path
from . import views

urlpatterns = [
    path('post/update_page/<int:post_pk>/', views.update_page),
    path('post/create/', views.create),
    path('post/', views.index),
]