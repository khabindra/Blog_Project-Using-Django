from django.urls import path
from .views import BlogListView,DetailView 
urlpatterns = [
    path('',BlogListView.as_view(),name='home'),
    path('post/<int:pk>',DetailView.as_view(),name='post_detail'),


]
