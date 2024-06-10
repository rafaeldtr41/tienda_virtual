from rest_framework import routers
from Book.views import *
from django.urls import path
from Book.models import Book_File, Pre_saved_PDF, Author, Book




router = routers.DefaultRouter()
router.register(r'pdfs', Pdf_Book_view, basename=Book_File)
router.register(r'not_reg_pdf', Pre_saved_PDF, basename=Pre_saved_PDF)
router.register(r'authors', Author_view, basename=Author)
router.register(r'books', Book_view, basename=Book)

urlpatterns = [

]

urlpatterns += router.urls
