from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('mangas', MangaViewSet, )

urlpatterns = [
    path('manga-list/', MangaListView.as_view()),
    path('manga-create/', MangaCreateView.as_view()),
    path('manga-list/<int:pk>/', MangaDetailView.as_view()),
    path('manga-update/<int:pk>/', MangaUpdateView.as_view()),
    path('manga-delete/<int:pk>/', MangaDeleteView.as_view()),
    path('saved-list/', SavedView.as_view()),
    path('category-list/', CategoryList.as_view()),
    path('tag-list/', TagList.as_view()),
    path('genre-list/', GenreList.as_view()),
    path('', include(router.urls)),
]
urlpatterns.extend(router.urls)
