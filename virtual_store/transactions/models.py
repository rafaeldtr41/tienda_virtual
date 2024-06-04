from django.db import models
from django.contrib.auth.models import User
from Book.models import Book




class Simple_User_articles(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)


class DATA_TRANSACTIONS(models.Model): #Admin access

    consumer_key = models.CharField(max_length=255, unique=True)
    consumer_secret = models.CharField(max_length=255, unique=True)
    merchant_op_id = models.CharField(max_length=255, unique=True)
    invoice_number = models.CharField(max_length=255, unique=True)
    terminal_id = models.CharField(max_length=255, unique=True)


class Pre_Buy_Book(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    esta_pagado = models.BooleanField(default=False)


class Buyed_Book(models.Model):

    buy = models.ForeignKey(Pre_Buy_Book, on_delete=models.CASCADE)
    #id_transaction



