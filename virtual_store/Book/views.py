from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.http import FileResponse
from Book.models import Book_File, Pre_saved_PDF, Author, Book, Preview_Book_File, concatenar_con_aleatorios
from Book.serializers import * 
from Book.pdf_handler import write_image, write_preview
from rest_framework.authentication import TokenAuthentication
from Book.permmisions import User_Books
from rest_framework import permissions
import random 
from pathlib import Path
import os




class Pdf_Book_view(viewsets.ModelViewSet):

    queryset = Book_File.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Book_File_serializer
    lookup_field = 'slug'
    permission_classes = []
    caching_class = None

    def create(self, request):

        try:
            file = request.FILES['file']
            
            aux = Book_File.objects.create(file = file)
            aux.save()
            name = concatenar_con_aleatorios('preview')
            preview, name = write_preview(file, name)
            dir = Path(__file__).resolve().parent.parent
            dir = dir / "media"
            dir = dir / name
            os.rename(preview, dir)
            aux1 = Preview_Book_File.objects.create(book_original=aux, file=name)
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

        self.queryset = Book_File.objects.all()
        slugs = [file_obj.slug for file_obj in self.queryset]

        return Response(slugs)

    def get_permissions(self):

        if not self.action == "retrieve":

            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

        else:

            return(permissions.IsAuthenticated(), User_Books())


class Preview_Book_File_view(viewsets.ModelViewSet):

    queryset = Preview_Book_File.objects.all()
    serializer_class = Preview_Book_File_serializer
    authentication_classes = (TokenAuthentication,)
    lookup_field = "slug"
    
    permission_classes = []

    def retrieve(self, request, *args, **kwargs):

        obj = self.get_object()
        path = obj.file.path
        return FileResponse(open(path, 'rb'))
    

class Pre_saved_PDF_view(viewsets.ModelViewSet):
#Nota estos son los pdf a medio guardar, primero se salvan en la base de datos y luego se introduce el autor y todas esas cosas.
    queryset = Pre_saved_PDF.objects.all()
    lookup_field = "id"
    authentication_classes = (TokenAuthentication,)
    serializer_class = Pre_saved_PDF_serializer
    permmisions_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def list(self, request, *args, **kwargs):

        slugs = []
        self.queryset = Pre_saved_PDF.objects.all()

        for i in self.queryset:

            dic = {}
            dic["id"] = i.id
            dic["file"] = i.pdf.slug
            dic["preview"] = i.preview_pdf.slug

            slugs.append(dic)

        return Response(slugs)

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        data = {"pdf": instance.pdf.slug, "preview": instance.preview_pdf.slug}
        return Response(data)


class Author_view(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = Author_serializer
    lookup_field = 'slug'
    authentication_classes = (TokenAuthentication,)
    permmisions_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class Book_view(viewsets.ModelViewSet):
# Cuando se vaya a salvar hay que pedir a pre_saved book el elemento y un autor
    queryset = Book.objects.all()
    serializer_class = Book_Serializer
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'slug'

     
    def retrieve(self, request, *args, **kwargs):
        
        response =super().retrieve(request, *args, **kwargs)
        obj = self.get_object()
        books = {"original": obj.book_file.slug, "preview": obj.preview_book.slug }
        response.data['books'] = books
        return response

    def get_permissions(self):

        if self.action == "create" or self.action == "delete" or self.action == "update":

            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

        else: 
            return []
        
class get_photo(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = Book_Serializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        return FileResponse(open(instance.image.path, 'rb'))
    
    

class Noticia_View(viewsets.ModelViewSet):

    queryset = Noticia.objects.all()
    serializer_class = Noticia_Serializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    authentication_classes = (TokenAuthentication,)

    def get_permissions(self):

        if self.action == "create" or self.action == "delete" or self.action == "update":

            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

        else: 
            return []


class Noticia_get_Photo_View(APIView):

    def get(self, request, slug):

        #try:

            aux = Noticia.objects.get(slug=slug)
            path = aux.imagen.path
            return FileResponse(open(path, 'rb'))
        
        #except:

            #return Response({"message":"Imagen no encontrada"}, status=404)


class get_free_books(APIView):

    def get(self, request):

        aux = Book.objects.filter(is_free=True)
        serializer = Book_Serializer(aux, many=True)
        return Response(serializer.data)
    

class get_non_free_books(APIView):

    def get(self, request):

        aux = Book.objects.filter(is_free=False)
        serializer = Book_Serializer(aux, many=True)
        return Response(serializer.data)

