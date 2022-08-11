from django.contrib import admin
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
   path('profile/', views.ProfileViewProfile.as_view(), name='view_profile'), 
   path('register/', views.ProfileRegisterUser.as_view(), name='register_user'),
   path('forgot-password/', views.ProfileForgotPassword.as_view(), name='forgot_password'),
   path('users/', views.UsersViewAll.as_view(), name='view_users'),
    path('users/<int:pk>/', views.UsersViewUser.as_view(), name='user_view'),
    path('users/edit/<int:pk>/', views.UsersEditUser.as_view(), name='user_edit'),
    path('users/delete/<int:pk>/', views.UsersDeleteUser.as_view(), name='user_delete'),
    path('users/create/', views.UsersCreateUser.as_view(), name='user_create'),

    path('users/invite/', views.UsersInviteUser.as_view(), name='user_invite'),
    path('users/reset-password/<int:pk>/', views.UsersResetPassword.as_view(), name='user_reset_password'),
    path('users/create-password/<uuid:uuid>/', views.UsersCreatePassword.as_view(), name='user_create_password'),
]
"""  path('users/', views.UsersViewAll.as_view(), name='users'),
    path('users/<int:pk>/', views.UsersViewUser.as_view(), name='user_view'),
    path('users/edit/<int:pk>/', views.UsersEditUser.as_view(), name='user_edit'),
    path('users/delete/<int:pk>/', views.UsersDeleteUser.as_view(), name='user_delete'),
    path('users/create/', views.UsersCreateUser.as_view(), name='user_create'),
    path('users/invite/', views.UsersInviteUser.as_view(), name='user_invite'),
    path('users/reset-password/<int:pk>/', views.UsersResetPassword.as_view(), name='user_reset_password'),
    path('users/create-password/<uuid:uuid>/', views.UsersCreatePassword.as_view(), name='user_create_password'),
    path('profile/<int:pk>/', views.ProfileViewProfile.as_view(), name='view_profile'), """