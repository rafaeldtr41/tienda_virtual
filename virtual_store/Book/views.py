from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.http import FileResponse
from Book.models import Book_File, Pre_saved_PDF, Author, Book, Preview_Book_File, concatenar_con_aleatorios
from Book.serializers import * 
from Book.pdf_handler import write_image, write_preview
import random




class Pdf_Book_view(viewsets.ModelViewSet):

    queryset = Book_File.objects.all()
    serializer_class = Book_File_serializer
    lookup_field = 'slug'
    permission_classes = []

    def create(self, request):

        try:
            file = request.FILES['file']
            
            aux = Book_File.objects.create(file = file)
            aux.save()
            name = concatenar_con_aleatorios('preview')
            preview = write_preview(file, name)
            aux1 = Preview_Book_File.objects.create(book_original=aux, file=preview)
            aux1.save()

            pre_saved = Pre_saved_PDF.objects.create(pdf=aux, preview_pdf=aux1)
            pre_saved.save()

            return Response(data={"message":"Pdf Saved"})

        except:

           return Response(data={"message":"Error Fetching File"})

    def retrieve(self, request, *args, **kwargs):

        obj = self.get_object()
        path = obj.file.path
        return FileResponse(open(path, 'rb'))

    def delete(self, request, *args, **kwargs):

        obj = self.get_object()
        obj.delete()
        return Response({"message":"Object Book file Deleted"})

    def list(self, request, *args, **kwargs):

        slugs = [file_obj.slug for file_obj in self.queryset]
        return Response(slugs)


class Preview_Book_File_view(viewsets.ModelViewSet):

    queryset = Preview_Book_File.objects.all()
    serializer_class = Preview_Book_File_serializer
    
    permission_classes = []

    def retrieve(self, request, *args, **kwargs):

        obj = self.get_object()
        path = obj.file.path
        return FileResponse(open(path, 'rb'))


class Pre_saved_PDF_view(viewsets.ModelViewSet):
#Nota estos son los pdf a medio guardar, primero se salvan en la base de datos y luego se introduce el autor y todas esas cosas.
    queryset = Pre_saved_PDF.objects.all()
    serializer_class = Pre_saved_PDF_serializer()

    def list(self, request, *args, **kwargs):

        slugs = []

        for i in self.queryset:

            dic = {}
            dic["file"] = i.pdf.slug
            dic["preview"] = i.preview_pdf.slug

            slugs.append(dic)

        return Response(slugs)

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


