from rest_framework import serializers

from .models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Arxiv_hujjatlar, Dissertatsiya


class AsarlarSerializer(serializers.ModelSerializer):
    jadid_fullname = serializers.SerializerMethodField()

    class Meta:
        model = Asarlar
        fields = ('id', 'title', 'jadid_fullname', 'jadid', 'create', 'update', 'image', 'file', 'count', 'likes',)

    def get_jadid_fullname(self, obj):
        return obj.jadid.fullname if obj.jadid else None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            if request:
                data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]
            else:
                data['files'] = [{'file': img.file.url} for img in files]

        return data


class AsarlarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asarlar
        fields = ['id', 'likes',]


class MaqolalarSerializer(serializers.ModelSerializer):
    jadid_fullname = serializers.SerializerMethodField()

    class Meta:
        model = Maqolalar
        fields = ('id', 'title', 'jadid_fullname', 'jadid', 'create', 'update', 'image', 'file', 'count', 'type',
                  'likes',)

    def get_jadid_fullname(self, obj):
        return obj.jadid.fullname if obj.jadid else None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data


class MaqolalarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqolalar
        fields = ['id', 'likes',]


class TadqiqotlarSerializer(serializers.ModelSerializer):
    jadid_fullname = serializers.SerializerMethodField()

    class Meta:
        model = Tadqiqotlar
        fields = ('id', 'title', 'jadid_fullname', 'create', 'update', 'image', 'file', 'type', 'count',)

    def get_jadid_fullname(self, obj):
        return obj.jadid.fullname if obj.jadid else None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data


class SherlarSerializer(serializers.ModelSerializer):
    jadid_fullname = serializers.SerializerMethodField()

    class Meta:
        model = Sherlar
        fields = ('id', 'title', 'jadid_fullname', 'jadid', 'create', 'update', 'image', 'file', 'type', 'count',
                  'likes',)

    def get_jadid_fullname(self, obj):
        return obj.jadid.fullname if obj.jadid else None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data


class SherlarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sherlar
        fields = ['id', 'likes',]


class HotiralarSerializer(serializers.ModelSerializer):
    jadid_fullname = serializers.SerializerMethodField()

    class Meta:
        model = Hotiralar
        fields = ('id', 'title', 'jadid_fullname', 'jadid', 'create', 'update', 'image', 'file', 'type', 'count',
                  'likes',)

    def get_jadid_fullname(self, obj):
        return obj.jadid.fullname if obj.jadid else None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data


class HotiralarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotiralar
        fields = ['id', 'likes',]


# class HikmatlarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hikmatlar
#         fields = ('id', 'text', 'create', 'update',)
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         files = instance.files.all()
#
#         if files:
#             request = self.context.get('request')
#             data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]
#
#         return data


class Arxiv_hujjatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arxiv_hujjatlar
        fields = ('id', 'title', 'type', 'image', 'file', 'count', 'likes',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data


class Arxiv_hujjatlarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arxiv_hujjatlar
        fields = ['id', 'likes',]


class DissertatsiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dissertatsiya
        fields = ('id', 'title', 'image', 'file', 'create', 'update', 'count', 'likes',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data


class DissertatsiyaLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dissertatsiya
        fields = ['id', 'likes',]