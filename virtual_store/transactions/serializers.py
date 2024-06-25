from django.contrib.auth.models import User
from rest_framework import serializers
from transactions.models import Pre_Buy_Book, DATA_TRANSACTIONS
from django.contrib.auth.hashers import make_password




class User_Serializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        # Hash the password before saving
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)


class DATA_TRANSACTIONS_serializer(serializers.ModelSerializer):

    class Meta:

        model = DATA_TRANSACTIONS
        fields = ["consumer_key", "consumer_secret", "merchant_op_id", "invoice_number", "terminal_id"]


class Pre_Buy_Book_serializer(serializers.ModelSerializer):

    slug = serializers.CharField(max_length=255)

    class Meta:

        model = Pre_Buy_Book
        fields = ["user", "esta_pagado"]