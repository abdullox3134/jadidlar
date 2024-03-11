from rest_framework import serializers
from manbalar.models import Videolar, Rasmlar, Audiolar


class VideolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videolar
        fields = ('id', 'title', 'video', 'link', 'file', 'create', 'update',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        videos = instance.video_files.all()

        if videos:
            request = self.context.get('request')
            data['videos'] = [{'video': request.build_absolute_uri(img.video.url)} for img in videos]
        return data


class RasmlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasmlar
        fields = ('id', 'title', 'image', 'create', 'update', 'blog_views', 'likes',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.rasimlar.all()

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data


class RasmlarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasmlar
        fields = ['id', 'likes',]


class AudiolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiolar
        fields = ('id', 'title', 'image', 'audio', 'create', 'update', 'likes',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        audios = instance.audio_files.all()
        print(audios)

        if audios:
            request = self.context.get('request')
            data['audios'] = [{'audio': request.build_absolute_uri(img.audio.url)} for img in audios]

        return data


class AudiolarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiolar
        fields = ['id', 'likes',]