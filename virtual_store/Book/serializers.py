from rest_framework import serializers
from Book.models import Book_File, Author, Book, Pre_saved_PDF



# aca estan los datos entrantes y salientes de la api
class Book_File_serializer(serializers.ModelSerializer):

    class Meta:

        model = Book_File
        lookup_field = 'slug'
        fields = ["file",]


class Author_serializer(serializers.ModelSerializer):

    class Meta:

        model = Author
        lookup_field = 'slug'
        fields = ["nombre", "apellido"]


class Book_Serializer(serializers.ModelSerializer):

    class Meta:
        
        model = Book
        lookup_field = 'slug'
        fields = ["name", "author", "Preview_Book", "Book_file", "price", "is_free"]


class Pre_saved_PDF_serializer(serializers.ModelSerializer):

    class Meta:
       
        model = Pre_saved_PDF
        fields = ['pdf, preview_pdf', 'imagen']
