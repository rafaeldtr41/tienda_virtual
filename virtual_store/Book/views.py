from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from Book.models import Book_File, Pre_saved_PDF, Author, Book, concatenar_con_aleatorios
from Book.serializers import * 




class Pdf_Book_view(viewsets.ModelViewSet):

    queryset = Book_File.objects.all()
    serializer_class = Book_File_serializer
    lookup_field = 'slug'

    def create(self, request):

        file = request.FILES['file']
        slug = concatenar_con_aleatorios('pdf_file')
        aux = Book_File.objects.create(file = file, slug=slug)
        aux.save()


class Pre_saved_PDF_view(viewsets.ModelViewSet):
#Nota estos son los pdf a medio guardar, primero se salvan en la base de datos y luego se introduce el autor y todas esas cosas.
    queryset = Pre_saved_PDF.objects.all()
    serializer_class = Pre_saved_PDF_serializer()
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class Author_view(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = Author_serializer
    lookup_field = 'slug'


class Book_view(viewsets.ModelViewSet):
# Cuando se vaya a salvar hay que pedir a pre_saved book el elemento y un autor
    queryset = Book.objects.all()
    serializer_class = Book_Serializer
    lookup_field = 'slug'


