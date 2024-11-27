from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
import django_filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .permissions import IsMangaCreator
from .serializers import *
from .models import *


class MangaFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title')
    category = django_filters.CharFilter(field_name='category')

    class Meta:
        model = Manga
        fields = ['title', 'category', ]



class MangaListView(generics.ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]
    filter_class = MangaFilter
    search_fields = ['title', 'category', ]


    def get_serializer_context(self):
        return {'request': self.request}


class MangaCreateView(generics.CreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [IsAuthenticated, ]


class MangaUpdateView(generics.UpdateAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [IsAuthenticated, IsMangaCreator]


class MangaDeleteView(generics.DestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [IsAuthenticated, IsMangaCreator]


class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'saved' or self.action == 'like':
            permissions = [IsAuthenticated, ]
        else:
            permissions = [IsMangaCreator, ]
        return [permissions() for permissions in permissions]


    @action(detail=True, methods=['POST'])
    def saved(self, requests, *args, **kwargs):
        manga = self.get_object()
        saved_obj, _ = Saved.objects.get_or_create(manga=manga, user=requests.user)
        saved_obj.saved = not saved_obj.saved
        saved_obj.save()
        status = 'Сохранено в избранные'
        if not saved_obj.saved:
            status = 'Удалено из избранных'
        return Response({'status': status})

    @action(detail=True, methods=['POST'])
    def like(self, requests, *args, **kwargs):
        manga = self.get_object()
        like_obj, _ = Like.objects.get_or_create(manga=manga, user=requests.user)
        like_obj.like = not like_obj.like
        like_obj.save()
        status = 'Поставил лайк'
        if not like_obj.like:
            status = 'Убрал лайк'
        return Response({'status': status})


    def get_serializer_context(self):
        return {'request': self.request}

class SavedView(generics.ListAPIView):
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer

class MangaDetailView(generics.RetrieveAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaDetailSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


