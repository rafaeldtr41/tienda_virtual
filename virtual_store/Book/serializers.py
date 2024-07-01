from rest_framework import serializers
from Book.models import Book_File, Author, Book, Pre_saved_PDF, Preview_Book_File, Noticia



# aca estan los datos entrantes y salientes de la api
class Book_File_serializer(serializers.ModelSerializer):

    class Meta:

        model = Book_File
        lookup_field = 'slug'
        fields = ["file", ]


class Preview_Book_File_serializer(serializers.ModelSerializer):

    
    class Meta:

        model = Preview_Book_File
        lookup_field = 'slug'
        fields = ("file", "slug", "book_original")

class Author_serializer(serializers.ModelSerializer):

    class Meta:

        model = Author
        lookup_field = 'slug'
        fields = ["nombre", "apellido", "slug"]


class Book_Serializer(serializers.ModelSerializer):

    preview_book = serializers.CharField(max_length=255)
    book_file = serializers.CharField(max_length=255)
    
    class Meta:
        
        model = Book
        lookup_field = 'slug'
        fields = ["name", "autor", "price", "is_free", "book_file", "preview_book", "slug", "image", "merchant_uuid", "description"]

    def create(self, validated_data):

        original = validated_data.pop('book_file', None)
        preview = validated_data.pop('preview_book', None)
        original_book = Book_File.objects.get(slug=original)
        preview_book = Preview_Book_File.objects.get(slug=preview)

        return Book.objects.create(preview_book=preview_book, book_file=original_book, **validated_data)



class Pre_saved_PDF_serializer(serializers.Serializer):

    class Meta:
       
        model = Pre_saved_PDF
        lookup_field = "id"
        fields = ['pdf, preview_pdf', 'id']


class Noticia_Serializer(serializers.ModelSerializer):

    class Meta: 

        model = Noticia
        lookup_field = "slug"
        fields = ["titulo", "texto", "slug", "imagen"]
