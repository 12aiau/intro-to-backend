from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),

    path('posts/<int:pk>/comments/add/', views.comment_add, name='comment_add'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/edit/', views.comment_edit, name='comment_edit'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]