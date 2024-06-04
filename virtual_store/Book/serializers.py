from rest_framework import serializers
from Book.models import Book_File, Author, Book



# aca estan los datos entrantes y salientes de la api
class Book_File_serializer(serializers.ModelSerializer):

    class Meta:

        model = Book_File
        fields = ["file",]


class Author_serializer(serializers.ModelSerializer):

    class Meta:

        model = Author
        fields = ["nombre", "apellido"]


class Book_Serialzer(serializers.ModelSerializer):

    class Meta:
        
        model = Book
        fields = ["name", "author", "Preview_Book", "Book_file", "price", "is_free"]

