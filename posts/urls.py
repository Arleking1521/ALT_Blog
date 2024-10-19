from django.urls import path
from .views import index, add_post, edit_post, delete_post

urlpatterns = [
    path('', index, name='post_list'),
    path('add/', add_post, name='add_post'),
    path('edit/<int:pid>/', edit_post, name='edit_post'),
    path('delete/<int:pid>/', delete_post, name='delete_post')
]

#http://127.0.0.1:8000/posts/