from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from ishtirokchilar.models import Ishtirokchilar
from ishtirokchilar.serializers import IshtirokchilarSerializer

from rest_framework.decorators import api_view
from rest_framework import filters


class IshtirokchilarListView(ListAPIView):
    search_fields = ['fullname']
    filter_backends = (filters.SearchFilter,)
    serializer_class = IshtirokchilarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Ishtirokchilar.objects.all().order_by('order')


@api_view(['GET'])
def ishtirokchilardetail(request, pk):
    ishtirokchilar = get_object_or_404(Ishtirokchilar, pk=pk)
    serializer = IshtirokchilarSerializer(ishtirokchilar, context={'request': request})
    return Response(serializer.data)
