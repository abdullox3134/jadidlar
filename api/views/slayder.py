from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from slayder.models import Slayder
from slayder.serializers import SlayderSerializer

from rest_framework.decorators import api_view
from rest_framework import filters


class SlayderListView(ListAPIView):
    search_fields = ['title', 'text']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SlayderSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Slayder.objects.all().order_by('-create')


@api_view(['GET'])
def slayderdetail(request, pk):
    slayder = get_object_or_404(Slayder, pk=pk)
    serializer = SlayderSerializer(slayder, context={'request': request})
    return Response(serializer.data)
