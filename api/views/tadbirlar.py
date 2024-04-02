from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.pagination import ResultsSetPagination
from tadbirlar.models import Kanferensiyalar, Seminarlar, Yangiliklar
from tadbirlar.serializers import KanferensiyalarSerializer, SeminarlarSerializer, YangiliklarSerializer, \
    YangiliklarLikeSerializer, SeminarlarLikeSerializer, KanferensiyalarLikeSerializer

from rest_framework.decorators import api_view
from rest_framework import filters, status


class KanferensiyalarListView(ListAPIView):
    search_fields = ['title', 'text']
    filter_backends = (filters.SearchFilter,)
    serializer_class = KanferensiyalarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Kanferensiyalar.objects.all().order_by('-created_at')


@api_view(['GET'])
def kanferensiyalardetail(request, pk):
    kanferensiyalar = get_object_or_404(Kanferensiyalar, pk=pk)
    kanferensiyalar.blog_views += 1
    kanferensiyalar.save()
    serializer = KanferensiyalarSerializer(kanferensiyalar, context={'request': request})
    return Response(serializer.data)


class KanferensiyalarLikeAPIView(RetrieveUpdateAPIView):
    queryset = Kanferensiyalar.objects.all()
    serializer_class = KanferensiyalarLikeSerializer

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
        return get_object_or_404(Kanferensiyalar, pk=pk)


class SeminarlarListView(ListAPIView):
    search_fields = ['title', 'text']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SeminarlarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Seminarlar.objects.all().order_by('-created_at')


@api_view(['GET'])
def seminarlardetail(request, pk):
    seminarlar = get_object_or_404(Seminarlar, pk=pk)
    seminarlar.blog_views += 1
    seminarlar.save()
    serializer = SeminarlarSerializer(seminarlar, context={'request': request})
    return Response(serializer.data)


class SeminarlarLikeAPIView(RetrieveUpdateAPIView):
    queryset = Seminarlar.objects.all()
    serializer_class = SeminarlarLikeSerializer

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
        return get_object_or_404(Seminarlar, pk=pk)


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
    yangiliklar.blog_views += 1
    yangiliklar.save()
    serializer = YangiliklarSerializer(yangiliklar, context={'request': request})
    return Response(serializer.data)


class YangiliklarLikeAPIView(RetrieveUpdateAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarLikeSerializer

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
        return get_object_or_404(Yangiliklar, pk=pk)
