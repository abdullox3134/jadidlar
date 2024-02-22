# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from tanlovlar.models import Tanlovlar
from tanlovlar.serializers import TanlovlarSerializer

from rest_framework.decorators import api_view
from rest_framework import filters


class TanlovlarListView(ListAPIView):
    search_fields = ['Telegram', 'Instagram', 'Facebook', 'Email', 'Telefon',]
    filter_backends = (filters.SearchFilter,)
    serializer_class = TanlovlarSerializer
    pagination_class = ResultsSetPagination

    # @swagger_auto_schema(
    #     manual_parameters=[
    #         openapi.Parameter('type', openapi.IN_QUERY, description='Filter by type', type=openapi.TYPE_STRING),
    #     ]
    # )

    def get_queryset(self):
        return Tanlovlar.objects.all()


@api_view(['GET'])
def tanlovlardetail(request, pk):
    tanlovlar = get_object_or_404(Tanlovlar, pk=pk)
    serializer = TanlovlarSerializer(tanlovlar, context={'request': request})
    return Response(serializer.data)
