from rest_framework import serializers
from sahifalar.models import Sahifalar


class SahifalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sahifalar
        fields = ('id', 'title', 'text', 'image', 'file', 'create', 'update', 'count',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data
