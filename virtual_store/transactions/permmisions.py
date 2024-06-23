from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission




class User_perm(BasePermission):

    def get_permissions(self, request, view, obj):

        return request.user.username == obj.username
