from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from sahifalar.models import Sahifalar
from sahifalar.serializers import SahifalarSerializer

from rest_framework.decorators import api_view
from rest_framework import filters


class SahifalarListView(ListAPIView):
    search_fields = ['title', 'text']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SahifalarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Sahifalar.objects.all().order_by('-create')


@api_view(['GET'])
def sahifalardetail(request, pk):
    sahifalar = get_object_or_404(Sahifalar, pk=pk)
    serializer = SahifalarSerializer(sahifalar, context={'request': request})
    return Response(serializer.data)
