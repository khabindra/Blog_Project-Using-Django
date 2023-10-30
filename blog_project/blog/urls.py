from django.urls import path
from .views import BlogListView,DetailView,BlogCreateView
urlpatterns = [
    path('',BlogListView.as_view(),name='home'),
    path('post/<int:pk>/',DetailView.as_view(),name='post_detail'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),



]
