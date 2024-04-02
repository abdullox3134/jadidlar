from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from manbalar.models import Audiolar, Videolar, Rasmlar
from manbalar.serializers import AudiolarSerializer, VideolarSerializer, RasmlarSerializer, AudiolarLikeSerializer, \
    RasmlarLikeSerializer

from rest_framework.decorators import api_view
from rest_framework import filters, status


class AudiolarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AudiolarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Audiolar.objects.all().order_by('-create')


@api_view(['GET'])
def audiolardetail(request, pk):
    audiolar = get_object_or_404(Audiolar, pk=pk)
    serializer = AudiolarSerializer(audiolar, context={'request': request})
    return Response(serializer.data)


class AudiolarLikeAPIView(RetrieveUpdateAPIView):
    queryset = Audiolar.objects.all()
    serializer_class = AudiolarLikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if user.is_authenticated:
            existing_like = instance.users.filter(id=user.id).exists()
            if not existing_like:
                instance.users.add(user)
                instance.likes += 1
            else:
                instance.users.remove(user)
                instance.likes -= 1
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Audiolar, pk=pk)


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
        return Rasmlar.objects.all().order_by('-create')


@api_view(['GET'])
def rasmlardetail(request, pk):
    rasmlar = get_object_or_404(Rasmlar, pk=pk)
    rasmlar.blog_views += 1
    rasmlar.save()
    serializer = RasmlarSerializer(rasmlar, context={'request': request})
    return Response(serializer.data)


class RasmlarLikeAPIView(RetrieveUpdateAPIView):
    queryset = Rasmlar.objects.all()
    serializer_class = RasmlarLikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if user.is_authenticated:
            existing_like = instance.users.filter(id=user.id).exists()
            if not existing_like:
                instance.users.add(user)
                instance.likes += 1
            else:
                instance.users.remove(user)
                instance.likes -= 1
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Rasmlar, pk=pk)