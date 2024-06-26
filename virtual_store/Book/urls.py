from rest_framework import routers
from Book.views import *
from django.urls import path
from Book.models import Book_File, Pre_saved_PDF, Author, Book, Preview_Book_File




router = routers.DefaultRouter()
router.register(r'pdfs', Pdf_Book_view, basename=Book_File)
router.register(r'not_reg_pdf', Pre_saved_PDF_view, basename=Pre_saved_PDF)
router.register(r'authors', Author_view, basename=Author)
router.register(r'books', Book_view, basename=Book)
router.register(r'preview_pdf', Preview_Book_File_view, basename=Preview_Book_File)
router.register(r'get_image', get_photo)

urlpatterns = [

]

urlpatterns += router.urls
