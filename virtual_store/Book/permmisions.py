from rest_framework.permissions import BasePermission
from transactions.models import Simple_User_articles
from Book.models import Book




class User_Books(BasePermission):

    def user_buy_the_book(self, request, view, obj):

        user = Simple_User_articles.objects.get(request.user)
        book = Book.objects.get(book_file=obj)
        try:
            
            aux = user.books.get(id=book)
            val = True

        except:
            
            val = False

        return val


