from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from manbalar.models import Audiolar, Videolar, Rasmlar
from manbalar.serializers import AudiolarSerializer, VideolarSerializer, RasmlarSerializer

from rest_framework.decorators import api_view
from rest_framework import filters


class AudiolarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AudiolarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Audiolar.objects.all()


@api_view(['GET'])
def audiolardetail(request, pk):
    audiolar = get_object_or_404(Audiolar, pk=pk)
    serializer = AudiolarSerializer(audiolar, context={'request': request})
    return Response(serializer.data)


class VideolarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = VideolarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Videolar.objects.all().order_by('-create')


@api_view(['GET'])
def videolardetail(request, pk):
    videolar = get_object_or_404(Videolar, pk=pk)
    serializer = VideolarSerializer(videolar, context={'request': request})
    return Response(serializer.data)


class RasmlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = RasmlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Rasmlar.objects.all()


@api_view(['GET'])
def rasmlardetail(request, pk):
    rasmlar = get_object_or_404(Rasmlar, pk=pk)
    serializer = RasmlarSerializer(rasmlar, context={'request': request})
    return Response(serializer.data)
