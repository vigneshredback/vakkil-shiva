from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('attorney/', views.attorney, name='attorney'),
    path('practice/', views.practice, name='practice'),
    path('contact/', views.contact, name='contact'),
    # path('practice/<slug:practice_slug>/', views.practice_detail, name='practice-detail'),
    path('practice-criminal-law/', views.practice_criminal_law, name='practice-criminal-law'),
    path('practice-civil-law/', views.practice_civil_law, name='practice-civil-law'),
    path('practice-family-law/', views.practice_family_law, name='practice-family-law'),
    path('practice-admiralty-maritime/', views.practice_admiralty_maritime_law, name='practice-admiralty-maritime'),
    path('practice-Antitrust-Competition/', views.practice_Antitrust_Competition_law, name='practice-Antitrust-Competition'),
    path('attorney-details/<int:id>', views.attorney_details, name='attorney-details'),
]