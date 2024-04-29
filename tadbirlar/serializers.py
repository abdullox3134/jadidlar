from rest_framework import serializers
from tadbirlar.models import Kanferensiyalar, Seminarlar, Yangiliklar


class KanferensiyalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanferensiyalar
        fields = ('id', 'title', 'text', 'image', 'created_at', 'updated_at', 'blog_views', 'likes',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.kanferensiya_images.all()
        print(images)

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data


class KanferensiyalarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanferensiyalar
        fields = ['id', 'likes',]


class SeminarlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminarlar
        fields = ('id', 'title', 'text', 'image', 'created_at', 'updated_at', 'blog_views', 'likes',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.seminar_images.all()
        print(images)

        if images:
            data['images'] = [{'image': img.image.url} for img in images]

        return data


class SeminarlarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminarlar
        fields = ['id', 'likes',]


class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = ('id', 'title', 'text', 'image', 'link', 'created_at', 'updated_at', 'blog_views', 'likes',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.yangilik_images.all()

        if images:
            data['images'] = [{'image': img.image.url} for img in images]

        return data


class YangiliklarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = ['id', 'likes',]