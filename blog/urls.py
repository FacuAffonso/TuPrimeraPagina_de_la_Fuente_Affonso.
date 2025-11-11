from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('authors/new/', views.create_author, name='create_author'),
    path('categories/new/', views.create_category, name='create_category'),
    path('posts/new/', views.create_post, name='create_post'),
    path('posts/', views.post_list, name='post_list'),
    path('search/', views.search_posts, name='search_posts'),
]
