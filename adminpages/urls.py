from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_index, name='admin-index'),
    path('create-team-member/', views.create_team_member, name='create-team-member'),
    path('update-team-member/<int:id>', views.update_team_member, name='update-team-member'),
    path('delete-team-member/<int:id>', views.delete_team_member, name='delete-team-member'),
    path('admin-login/', views.admin_login, name='admin-login'),
    path('admin-logout/', views.admin_logout, name='admin-logout'),
]