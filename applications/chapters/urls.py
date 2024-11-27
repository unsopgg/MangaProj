from django.urls import path
from .views import *


urlpatterns = [
    path('chapter-create/', ChapterCreateView.as_view()),
    path('chapter-update/<int:pk>/', ChapterUpdateView.as_view()),
    path('chapter-delete/<int:pk>/', ChapterDeleteView.as_view()),
    path('chapter/<int:pk>/', ChapterView.as_view()),
]