from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_feed, name='home_feed'),
    path('profiles/', views.profiles_list, name='profiles_list'),
    path('user/<str:username>/', views.user_profile_view, name='user_profile_view'),
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    path('follow/<int:profile_id>/', views.toggle_follow, name='toggle_follow'),
]