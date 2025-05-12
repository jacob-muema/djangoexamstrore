from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),  # Route for user login
    path('logout/', views.user_logout, name='logout'),  # Route for user logout
    path('upload/', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
]
