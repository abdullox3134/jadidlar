from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from tadbirlar.models import Kanferensiyalar, Seminarlar, Yangiliklar
from tadbirlar.serializers import KanferensiyalarSerializer, SeminarlarSerializer, YangiliklarSerializer

from rest_framework.decorators import api_view
from rest_framework import filters


class KanferensiyalarListView(ListAPIView):
    search_fields = ['title', 'text']
    filter_backends = (filters.SearchFilter,)
    serializer_class = KanferensiyalarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Kanferensiyalar.objects.all()


@api_view(['GET'])
def kanferensiyalardetail(request, pk):
    kanferensiyalar = get_object_or_404(Kanferensiyalar, pk=pk)
    serializer = KanferensiyalarSerializer(kanferensiyalar, context={'request': request})
    return Response(serializer.data)


class SeminarlarListView(ListAPIView):
    search_fields = ['title', 'text']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SeminarlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Seminarlar.objects.all()


@api_view(['GET'])
def seminarlardetail(request, pk):
    seminarlar = get_object_or_404(Seminarlar, pk=pk)
    serializer = SeminarlarSerializer(seminarlar, context={'request': request})
    return Response(serializer.data)


class YangiliklarListView(ListAPIView):
    search_fields = ['title', 'text']
    filter_backends = (filters.SearchFilter,)
    serializer_class = YangiliklarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Yangiliklar.objects.all().order_by('-created_at')


@api_view(['GET'])
def yangiliklardetail(request, pk):
    yangiliklar = get_object_or_404(Yangiliklar, pk=pk)
    serializer = YangiliklarSerializer(yangiliklar, context={'request': request})
    return Response(serializer.data)