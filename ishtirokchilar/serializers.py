from rest_framework import serializers
from ishtirokchilar.models import Ishtirokchilar


class IshtirokchilarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ishtirokchilar
        fields = ('id', 'fullname_uz', 'fullname_ru', 'fullname_en', 'position_uz', 'position_ru', 'position_en',
                  'image', 'order',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.ishtirokchi_images.all()

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data
