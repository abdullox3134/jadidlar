import random

from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from api.pagination import ResultsSetPagination
from jadidlar.models import Jadid
from jadidlar.serializers import JadidSerializer
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.response import Response


class JadidlarListView(ListAPIView):
    search_fields = ['fullname',]
    filter_backends = (filters.SearchFilter,)
    serializer_class = JadidSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Jadid.objects.all().order_by('order')


@api_view(['GET'])
def get_random_jadid(request):
    fifteen_records = list(Jadid.objects.order_by('order')[:15])
    random.shuffle(fifteen_records)
    serializer = JadidSerializer(fifteen_records, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def jadidlardetail(request, pk):
    jadidlar = get_object_or_404(Jadid, pk=pk)
    jadidlar.blog_views += 1
    jadidlar.save()
    serializer = JadidSerializer(jadidlar, context={'request': request})
    return Response(serializer.data)