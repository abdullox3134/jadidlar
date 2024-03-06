from hujjatlar.serializers import AsarlarSerializer, MaqolalarSerializer, TadqiqotlarSerializer, SherlarSerializer, \
    HotiralarSerializer
from jadidlar.models import Jadid
from hikmatli_sozlar.serializers import Hikmatli_sozlarSerializer
from rest_framework import serializers


class JadidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jadid
        fields = ('id', 'fullname', 'image', 'bio', 'birthday', 'die_day', 'order', 'create', 'update',
                  'blog_views', 'hikmatli_sozlar', 'asarlar', 'maqolalar', 'tadqiqotlar', 'sherlar', 'hotiralar',)

    def to_representation(self, instance):
        request = self.context.get('request')
        data = super().to_representation(instance)
        images = instance.jadid_images.all()
        hikmatli_sozlarlar = instance.hikmatli_sozlar.all()
        asarlar = instance.asarlar.all()
        maqolalar = instance.maqolalar.all()
        tadqiqotlar = instance.tadqiqotlar.all()
        sherlar = instance.sherlar.all()
        hotiralar = instance.hotiralar.all()

        base_url = request.build_absolute_uri('/')[:-1]

        if hikmatli_sozlarlar:
            data['hikmatli_sozlar'] = Hikmatli_sozlarSerializer(hikmatli_sozlarlar, many=True).data

        if asarlar:
            data['asarlar'] = AsarlarSerializer(asarlar, many=True).data
            if 'asarlar' in data:
                for asar in data['asarlar']:
                    if 'file' in asar and asar['file']:
                        asar['file'] = base_url + asar['file']
                    if 'image' in asar and asar['image']:
                        asar['image'] = base_url + asar['image']

        if maqolalar:
            data['maqolalar'] = MaqolalarSerializer(maqolalar, many=True).data
            if 'maqolalar' in data:
                for maqola in data['maqolalar']:
                    if 'file' in maqola and maqola['file']:
                        maqola['file'] = base_url + maqola['file']
                    if 'image' in maqola and maqola['image']:
                        maqola['image'] = base_url + maqola['image']

        if tadqiqotlar:
            data['tadqiqotlar'] = TadqiqotlarSerializer(tadqiqotlar, many=True).data
            if 'tadqiqotlar' in data:
                for tadqiqot in data['tadqiqotlar']:
                    if 'file' in tadqiqot and tadqiqot['file']:
                        tadqiqot['file'] = base_url + tadqiqot['file']
                    if 'image' in tadqiqot and tadqiqot['image']:
                        tadqiqot['image'] = base_url + tadqiqot['image']

        if sherlar:
            data['sherlar'] = SherlarSerializer(sherlar, many=True).data
            if 'sherlar' in data:
                for sher in data['sherlar']:
                    if 'file' in sher and sher['file']:
                        sher['file'] = base_url + sher['file']
                    if 'image' in sher and sher['image']:
                        sher['image'] = base_url + sher['image']

        if hotiralar:
            data['hotiralar'] = HotiralarSerializer(hotiralar, many=True).data
            if 'hotiralar' in data:
                for hotira in data['hotiralar']:
                    if 'file' in hotira and hotira['file']:
                        hotira['file'] = base_url + hotira['file']
                    if 'image' in hotira and hotira['image']:
                        hotira['image'] = base_url + hotira['image']

        if images:
            data['images'] = [{'image': base_url + img.image.url} for img in images]

        return data
