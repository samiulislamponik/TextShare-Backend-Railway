from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [

    path('text/', views.create_text_snippet, name='create_text_snippet'),
    path('text/<str:url>/', views.retrieve_text_snippet, name='retrieve_text_snippet'),
    path('text/<str:url>/edit/', views.update_text_snippet, name='update_text_snippet'),
    
]