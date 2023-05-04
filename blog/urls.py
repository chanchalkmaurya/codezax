from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact', views.contact, name='about'),
    path('author/<int:author_id>', views.author, name='author_detail'),
    path('author_list', views.author_list, name='author_list'),
    path('post/<int:blog_id>', views.post, name="post_detail")
]
