from rest_framework import serializers
from .models import *
from ..chapters.serializers import *
from ..comment.serializers import CommentSerializer

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class SavedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Saved
        fields = ('manga', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['manga'] = f'{instance.manga}'
        return representation

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ('id', 'title', 'status', )

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['creator_id'] = request.user.id
        manga = Manga.objects.create(**validated_data)
        return manga

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_rating = [i.rating for i in instance.comment.all()]
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        return representation


class MangaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
                print(url)
        else:
            url = ''
        return url


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class MangaDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manga
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_rating = [i.rating for i in instance.comment.all()]
        representation['like'] = instance.like.filter(like=True).count()
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        representation['comments'] = CommentSerializer(instance.comment.filter(manga=instance.id), many=True).data
        representation['genre'] = f'{instance.genre}'
        representation['tag'] = f'{instance.tag}'
        representation['category'] = f'{instance.category}'
        representation['chapter'] = ChapterNameSerializer(instance.chapter.filter(manga=instance.id), many=True).data
        return representation