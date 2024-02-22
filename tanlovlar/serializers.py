from rest_framework import serializers
from tanlovlar.models import Tanlovlar


class TanlovlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanlovlar
        fields = ('Telegram', 'Instagram', 'Facebook', 'Email', 'Telefon',)
