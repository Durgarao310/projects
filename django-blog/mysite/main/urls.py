from django.urls import path
from main import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('post/',views.post_list, name='post-list'),
    path("post/<int:pk>/like",views.post_like, name="post-like"),
    path('post/<int:pk>/',views.post_detail, name='post-detail'),
    path('post/<int:pk>/remove/',views.post_remove, name='post-delete'),
    path('post/<int:pk>/edit/',views.post_edit, name='post-edit'),
    path('post/new/',views.post_new, name='post-new'),
    path('post/<int:pk>/comment/add/',views.add_comment_to_post, name='comment-post'),
    path('post/<int:pk>/comment/remove/',views.comment_remove, name='comment-remove'),
    path('about/',views.about, name='about'),
]
