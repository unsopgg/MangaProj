from rest_framework import serializers

from .models import Chapter

class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = ('title', 'manga', 'image', 'id', )

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['creator_id'] = request.user.id
        manga = Chapter.objects.create(**validated_data)
        return manga

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

class ChapterNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = ('title', )