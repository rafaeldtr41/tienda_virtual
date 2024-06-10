from django.contrib import admin
from Book.models import Book_File, Book, Author

admin.site.register(Book_File)
admin.site.register(Book)
admin.site.register(Author)
