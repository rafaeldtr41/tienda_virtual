from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout
from transactions.serializers import *
from transactions.models import *
from Book.models import Book
from enzona_api.enzona_business_payment import enzona_business_payment




class User_View(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = User_Serializer


class Logout_View(APIView):

    def get(self, request, format=None):

        logout(request)
        return Response(status=200)


class DATA_TRANSACTIONS_view(viewsets.ModelViewSet):

    queryset = DATA_TRANSACTIONS.objects.all()
    serializer_class = DATA_TRANSACTIONS_serializer


class Pre_Buy_Book_View(viewsets.ModelViewSet):

    queryset = Pre_Buy_Book.objects.all()
    serializer_class = Pre_Buy_Book_serializer

    def create(self, validated_data, request):

        aux = validated_data.pop("slug", None)
        try:
            aux = Book.objects.get(slug=aux)

        except:

            return Response({"Error":"Book not exist"})
        
        return Pre_Buy_Book.objects.create(user=request.user, book=aux)


#sin testear
class Pay(APIView):

    def get(self, request, format=None):

        user = request.user
        data_t = DATA_TRANSACTIONS.objects.all()
        data_t = data_t.pop()
        pre_buy = Pre_Buy_Book.objects.get(user=user) 
        book = pre_buy.book
        
        ebp = enzona_business_payment(data_t.consumer_key, data_t.consumer_secret)

        merchant_uuid = book.merchant_uuid #your merchant_uuid

        SHIPPING = 10
        DISCOUNT = 2.0
        TIP = 5.0
        MERCHANT_OP_ID = data_t.merchant_op_id #your market identifier
        INVOICE_NUMBER = data_t.invoice_number #invoice number
        TERMINAL_ID = data_t.terminal_id #terminal identifier (POS, Cash Register, etc.)

        product1 = Product(name=book.name, description="description1", quantity=1, price=book.price, tax=20.18)

        lst_products = [product1.get_product()]

        pay = Payments(
    
            merchant_uuid=merchant_uuid,
            description_payment= "Description pay",
            currency="CUP",
            shipping=SHIPPING,
            discount=DISCOUNT,
            tip=TIP,
            lst_products=lst_products,
            merchant_op_id=MERCHANT_OP_ID,
            invoice_number=INVOICE_NUMBER,
            return_url=URL_RETURN,
            cancel_url=URL_CANCEL,
            terminal_id=TERMINAL_ID
        )

        response = ebp.create_payments(payment=pay.get_payment())
        transaction_uuid = response.transaction_uuid()
        link_confirm = response.link_confirm()

        aux = Buyed_Book.objects.create(buy=pre_buy)
        aux.save()
        simple_user = Simple_User_articles.objects.get(user=user)
        simple_user.books.add(book)
        simple_user.books.save()
