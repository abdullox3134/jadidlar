from django.http import FileResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from hujjatlar.models import Maqolalar, Asarlar, Tadqiqotlar, Sherlar, Hotiralar, Arxiv_hujjatlar, \
    Dissertatsiya
from sahifalar.models import Sahifalar


class FileDownAsarView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            file_instance = Asarlar.objects.get(id=pk)
        except Asarlar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_instance.count += 1
        file_instance.save()
        response = {
            "path": request.build_absolute_uri(file_instance.file.url)
        }
        return Response(response, status=status.HTTP_200_OK)


class FileDownMaqolaView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            file_instance = Maqolalar.objects.get(id=pk)
        except Maqolalar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_instance.count += 1
        file_instance.save()
        response = {
            "path": request.build_absolute_uri(file_instance.file.url)
        }
        return Response(response, status=status.HTTP_200_OK)


class FileDownTadqiqotView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            file_instance = Tadqiqotlar.objects.get(id=pk)
        except Tadqiqotlar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_instance.count += 1
        file_instance.save()
        response = {
            "path": request.build_absolute_uri(file_instance.file.url)
        }
        return Response(response, status=status.HTTP_200_OK)


class FileDownSherView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            file_instance = Sherlar.objects.get(id=pk)
        except Sherlar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_instance.count += 1
        file_instance.save()
        response = {
            "path": request.build_absolute_uri(file_instance.file.url)
        }
        return Response(response, status=status.HTTP_200_OK)


class FileDownHotiraView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            file_instance = Hotiralar.objects.get(id=pk)
        except Hotiralar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_instance.count += 1
        file_instance.save()
        response = {
            "path": request.build_absolute_uri(file_instance.file.url)
        }
        return Response(response, status=status.HTTP_200_OK)


class FileDownArxiv_hujjatView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            file_instance = Arxiv_hujjatlar.objects.get(id=pk)
        except Arxiv_hujjatlar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_instance.count += 1
        file_instance.save()
        response = {
            "path": request.build_absolute_uri(file_instance.file.url)
        }
        return Response(response, status=status.HTTP_200_OK)


class FileDownDissertatsiyaView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            file_instance = Dissertatsiya.objects.get(id=pk)
        except Dissertatsiya.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_instance.count += 1
        file_instance.save()
        response = {
            "path": request.build_absolute_uri(file_instance.file.url)
        }
        return Response(response, status=status.HTTP_200_OK)


class FileDownSahifaView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            file_instance = Sahifalar.objects.get(id=pk)
        except Sahifalar.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_instance.count += 1
        file_instance.save()
        response = {
            "path": request.build_absolute_uri(file_instance.file.url)
        }
        return Response(response, status=status.HTTP_200_OK)
