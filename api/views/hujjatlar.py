from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from hujjatlar.models import Asarlar, Maqolalar, Tadqiqotlar, Sherlar, Hotiralar, Arxiv_hujjatlar, \
    Dissertatsiya
from hujjatlar.serializers import AsarlarSerializer, MaqolalarSerializer, TadqiqotlarSerializer, SherlarSerializer, \
    HotiralarSerializer, Arxiv_hujjatlarSerializer, DissertatsiyaSerializer, Arxiv_hujjatlarLikeSerializer, \
    MaqolalarLikeSerializer, AsarlarLikeSerializer, DissertatsiyaLikeSerializer, HotiralarLikeSerializer, \
    SherlarLikeSerializer

from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import filters, status


class AsarlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AsarlarSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jadid__id', "turkiston_muxtoriyati", "til_va_imlo", "tadqiqotlar"]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Asarlar.objects.all()


@api_view(['GET'])
def asarlardetail(request, pk):
    asarlar = get_object_or_404(Asarlar, pk=pk)
    serializer = AsarlarSerializer(asarlar, context={'request': request})
    return Response(serializer.data)


class AsarlarLikeAPIView(RetrieveUpdateAPIView):
    queryset = Asarlar.objects.all()
    serializer_class = AsarlarLikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if user.is_authenticated:
            existing_like = instance.likes.filter(id=user.id).exists()
            if not existing_like:
                instance.likes.add(user)
            else:
                instance.likes.remove(user)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Asarlar, pk=pk)


class MaqolalarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MaqolalarSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jadid__id', "turkiston_muxtoriyati", "til_va_imlo", "tadqiqotlar", "type",]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Maqolalar.objects.all()


@api_view(['GET'])
def maqolalardetail(request, pk):
    maqolalar = get_object_or_404(Maqolalar, pk=pk)
    serializer = MaqolalarSerializer(maqolalar, context={'request': request})
    return Response(serializer.data)


class MaqolalarLikeAPIView(RetrieveUpdateAPIView):
    queryset = Maqolalar.objects.all()
    serializer_class = MaqolalarLikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if user.is_authenticated:
            existing_like = instance.likes.filter(id=user.id).exists()
            if not existing_like:
                instance.likes.add(user)
            else:
                instance.likes.remove(user)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Maqolalar, pk=pk)



class TadqiqotlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = TadqiqotlarSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jadid__id', ]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('type', openapi.IN_QUERY, description='Filter by type', type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        type_param = self.request.query_params.get('type', None)
        if type_param:
            return Tadqiqotlar.objects.filter(type=type_param)
        else:
            return Tadqiqotlar.objects.all()


@api_view(['GET'])
def tadqiqotlardetail(request, pk):
    tadqiqotlar = get_object_or_404(Tadqiqotlar, pk=pk)
    serializer = TadqiqotlarSerializer(tadqiqotlar, context={'request': request})
    return Response(serializer.data)


class SherlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SherlarSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jadid__id', ]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('type', openapi.IN_QUERY, description='Filter by type', type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        type_param = self.request.query_params.get('type', None)
        if type_param:
            return Sherlar.objects.filter(type=type_param)
        else:
            return Sherlar.objects.all()


@api_view(['GET'])
def sherlardetail(request, pk):
    sherlar = get_object_or_404(Sherlar, pk=pk)
    serializer = SherlarSerializer(sherlar, context={'request': request})
    return Response(serializer.data)


class SherlarLikeAPIView(RetrieveUpdateAPIView):
    queryset = Sherlar.objects.all()
    serializer_class = SherlarLikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if user.is_authenticated:
            existing_like = instance.likes.filter(id=user.id).exists()
            if not existing_like:
                instance.likes.add(user)
            else:
                instance.likes.remove(user)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Sherlar, pk=pk)


class HotiralarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = HotiralarSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['jadid__id', ]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('type', openapi.IN_QUERY, description='Filter by type', type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        type_param = self.request.query_params.get('type', None)
        if type_param:
            return Hotiralar.objects.filter(type=type_param)
        else:
            return Hotiralar.objects.all()


@api_view(['GET'])
def hotiralardetail(request, pk):
    hotiralar = get_object_or_404(Hotiralar, pk=pk)
    serializer = HotiralarSerializer(hotiralar, context={'request': request})
    return Response(serializer.data)


class HotiralarLikeAPIView(RetrieveUpdateAPIView):
    queryset = Hotiralar.objects.all()
    serializer_class = HotiralarLikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if user.is_authenticated:
            existing_like = instance.likes.filter(id=user.id).exists()
            if not existing_like:
                instance.likes.add(user)
            else:
                instance.likes.remove(user)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Hotiralar, pk=pk)


class Arxiv_hujjatlarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = Arxiv_hujjatlarSerializer
    pagination_class = ResultsSetPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('type', openapi.IN_QUERY, description='Filter by type', type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        type_param = self.request.query_params.get('type', None)
        if type_param:
            return Arxiv_hujjatlar.objects.filter(type=type_param)
        else:
            return Arxiv_hujjatlar.objects.all()


@api_view(['GET'])
def arxiv_hujjatlardetail(request, pk):
    arxiv_hujjatlar = get_object_or_404(Arxiv_hujjatlar, pk=pk)
    serializer = Arxiv_hujjatlarSerializer(arxiv_hujjatlar, context={'request': request})
    return Response(serializer.data)


class Arxiv_hujjatlarLikeAPIView(RetrieveUpdateAPIView):
    queryset = Arxiv_hujjatlar.objects.all()
    serializer_class = Arxiv_hujjatlarLikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if user.is_authenticated:
            existing_like = instance.likes.filter(id=user.id).exists()
            if not existing_like:
                instance.likes.add(user)
            else:
                instance.likes.remove(user)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Arxiv_hujjatlar, pk=pk)


class DissertatsiyaListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = DissertatsiyaSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Dissertatsiya.objects.all()


@api_view(['GET'])
def dissertatsiyadetail(request, pk):
    dissertatsiya = get_object_or_404(Dissertatsiya, pk=pk)
    serializer = DissertatsiyaSerializer(dissertatsiya, context={'request': request})
    return Response(serializer.data)


class DissertatsiyaLikeAPIView(RetrieveUpdateAPIView):
    queryset = Dissertatsiya.objects.all()
    serializer_class = DissertatsiyaLikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if user.is_authenticated:
            existing_like = instance.likes.filter(id=user.id).exists()
            if not existing_like:
                instance.likes.add(user)
            else:
                instance.likes.remove(user)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Dissertatsiya, pk=pk)