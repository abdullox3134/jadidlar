from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from api.pagination import ResultsSetPagination
from jadidlar.models import Jadid
from jadidlar.serializers import JadidSerializer, LikeSerializer
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework import generics
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


# class LikeListCreate(APIView):
#
#     def get(self, request, pk):
#         # Get the Jadid object based on the URL parameter
#         jadid = get_object_or_404(Jadid, pk=pk)
#
#         # Count the number of likes for the Jadid object
#         like_count = jadid.likes.count()
#
#         # Serialize the like count
#         serializer = PostlikeSerializer({'like_count': like_count})
#
#         # Return the serialized data
#         return Response(serializer.data)
#
#     def post(self, request, pk):
#         # Get the Jadid object based on the URL parameter
#         jadid = get_object_or_404(Jadid, pk=pk)
#
#         # Check if the user has already liked the post
#         if jadid.likes.filter(user=request.user).exists():
#             return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # Create a new Like object for the Jadid object
#         like = Like.objects.create(user=request.user, jadid=jadid)
#
#         # Serialize the new like object
#         serializer = PostlikeSerializer(like)
#
#         # Return the serialized data
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class LikeAPIView(generics.CreateAPIView):
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_authenticated:  # Foydalanuvchi avtorizatsiyadan o'tganligini tekshiramiz
            user = request.user
            existing_like = instance.likes.filter(id=user.id).exists()
            if not existing_like:
                instance.likes.add(user)
                instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"})
#
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Jadid, pk=pk)


# class LikeAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = LikeSerializer
#
#     def put(self, request, *args, **kwargs):
#         instance = self.get_object()
#         user = request.user
#         # Foydalanuvchi bir marta bitta "like" tugmasini bosganligini tekshirish
#         existing_like = instance.like_set.filter(user=user).exists()
#         if not existing_like:
#             instance.like_count += 1  # Like sonini oshirish
#             instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)






