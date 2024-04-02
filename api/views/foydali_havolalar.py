from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from foydali_havolalar.models import Foydali_havolalar
from foydali_havolalar.serializers import Foydali_havolalarSerializer

from rest_framework.decorators import api_view
from rest_framework import filters


class Foydali_havolalarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Foydali_havolalarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Foydali_havolalar.objects.all()


@api_view(['GET'])
def foydali_havolalardetail(request, pk):
    foydali_havolalar = get_object_or_404(Foydali_havolalar, pk=pk)
    serializer = Foydali_havolalarSerializer(foydali_havolalar, context={'request': request})
    return Response(serializer.data)
