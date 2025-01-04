from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('attorney/', views.attorney, name='attorney'),
    path('attorney-details/<int:id>', views.attorney_details, name='attorney-details'),
]