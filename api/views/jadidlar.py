from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from django.shortcuts import get_object_or_404
from api.pagination import ResultsSetPagination
from jadidlar.models import Jadid
from jadidlar.serializers import JadidSerializer, LikeSerializer
from rest_framework.decorators import api_view
from rest_framework import filters
# from rest_framework import generics
from rest_framework.response import Response


class JadidlarListView(ListAPIView):
    search_fields = ['fullname', 'bio']
    filter_backends = (filters.SearchFilter,)
    serializer_class = JadidSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Jadid.objects.all().order_by('order')


@api_view(['GET'])
def jadidlardetail(request, pk):
    jadidlar = get_object_or_404(Jadid, pk=pk)
    serializer = JadidSerializer(jadidlar, context={'request': request})
    return Response(serializer.data)


class LikeAPIView(RetrieveUpdateAPIView):
    queryset = Jadid.objects.all()
    serializer_class = LikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_authenticated:
            user = request.user
            existing_like = instance.likes.filter(id=user.id).exists()
            if not existing_like:
                instance.likes.add(user)
                instance.save()
                instance.blog_views += 1
                instance.save()
            else:
                instance.likes.remove(user)
                instance.save()
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"})

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Jadid, pk=pk)

    def blog_post(request, post_id):
        # your code
        blog_object = Jadid.objects.get(id=post_id)
        blog_object.blog_views = blog_object.blog_views + 1
        blog_object.save()






