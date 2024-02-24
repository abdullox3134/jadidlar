from rest_framework import serializers

from .models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Arxiv_hujjatlar, Dissertatsiya

# from django.conf import settings


class AsarlarSerializer(serializers.ModelSerializer):
    jadid_fullname = serializers.SerializerMethodField()

    class Meta:
        model = Asarlar
        fields = ('id', 'title', 'jadid_fullname', 'jadid', 'create', 'update', 'image', 'file', 'count',)

    def get_jadid_fullname(self, obj):
        return obj.jadid.fullname if obj.jadid else None

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     files = instance.files.all()
    #
    #     if files:
    #         request = self.context.get('request')
    #         data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]
    #
    #     return data
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


class MaqolalarSerializer(serializers.ModelSerializer):
    jadid_fullname = serializers.SerializerMethodField()

    class Meta:
        model = Maqolalar
        fields = ('id', 'title', 'jadid_fullname', 'jadid', 'create', 'update', 'image', 'file', 'count', 'type')

    def get_jadid_fullname(self, obj):
        return obj.jadid.fullname if obj.jadid else None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data


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
        fields = ('id', 'title', 'jadid_fullname', 'jadid', 'create', 'update', 'image', 'file', 'type', 'count',)

    def get_jadid_fullname(self, obj):
        return obj.jadid.fullname if obj.jadid else None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data


class HotiralarSerializer(serializers.ModelSerializer):
    jadid_fullname = serializers.SerializerMethodField()

    class Meta:
        model = Hotiralar
        fields = ('id', 'title', 'jadid_fullname', 'jadid', 'create', 'update', 'image', 'file', 'type', 'count',)

    def get_jadid_fullname(self, obj):
        return obj.jadid.fullname if obj.jadid else None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data


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
        fields = ('id', 'title', 'type', 'image', 'file', 'count',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data


class DissertatsiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dissertatsiya
        fields = ('id', 'title', 'image', 'file', 'create', 'update', 'count',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        files = instance.files.all()

        if files:
            request = self.context.get('request')
            data['files'] = [{'file': request.build_absolute_uri(img.file.url)} for img in files]

        return data