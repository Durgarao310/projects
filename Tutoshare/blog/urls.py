from django.urls import path
from .views import list_tech, tech_detail, tech_create, tut_create, register,tut_upvote,tut_unupvote
from django.contrib.auth import views 

urlpatterns = [
    path('', list_tech, name='list_tech'),
    path('<int:pk>/', tech_detail, name="tech_detail"),
    path('tech/create/', tech_create,name="tech_create"),
    path('tut/create', tut_create, name="tut_create"),
    path('tut/<int:pk>/upvote/', tut_upvote, name="tut_upvote"),
    path('tut/<int:pk>/unupvote/', tut_unupvote, name="tut_unupvote"),
    path('register/', register, name="register"),
    path('login/', views.LoginView.as_view(template_name='blog/login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(template_name='blog/logout.html'), name="logout"),
]