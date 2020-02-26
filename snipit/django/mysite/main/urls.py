from django.urls import path
from .views import (
    PostListView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/',views.post_new, name="add-post"),
    path('post/<int:pk>/detail/',views.post_detail, name="post-detail"),
    path('post/<int:pk>/delete/',views.post_delete, name="post-delete"),
    path('post/<int:pk>edit/',views.post_edit, name="post-edit"),
    path('post/<int:pk>/likes/',views.post_like, name="post-like"),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/add/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),


]