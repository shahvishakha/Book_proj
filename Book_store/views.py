from operator import is_
from urllib import response
from django.shortcuts import render
from uritemplate import partial

# Create your views here.
from Book_store.models import Book_store

from rest_framework.viewsets import ModelViewSet

from Book_store.serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated




class BookStoreView(ModelViewSet):
    queryset = Book_store.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
  
    def put(self, request, pk, format=None):
        book_obj = Book_store.objects.get(id=pk)
        serializer = BookSerializer(book_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    @action(methods=['get'],url_name='get-book-price', detail=True)
    def get_total_price(self, request, pk=None):
        book_obj = Book_store.objects.get(id=pk)
        resp = book_obj.get_total_price()
        python_dict = {"Book Price":resp}
        print(python_dict)
        return JsonResponse(python_dict)

   