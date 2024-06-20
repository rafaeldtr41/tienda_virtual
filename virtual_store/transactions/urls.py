from django.urls import path
from django.contrib.auth.models import User
from rest_framework import routers
from transactions.views import *
from transactions.models import *




router = routers.DefaultRouter()
router.register(r'user_reg', User_View, basename=User),
router.register(r'data_transaction', DATA_TRANSACTIONS_view, basename=DATA_TRANSACTIONS)

urlpatterns = [
    path('logout/', Logout_View.as_view(), name="logout"),
    path('pay/', Pay.as_view(), name="pay"),
    ]

urlpatterns += router.urls
