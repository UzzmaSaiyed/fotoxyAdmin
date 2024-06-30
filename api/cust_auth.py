from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from .models import *

class CustomJWTAuthentication(JWTAuthentication):
    def get_user_id(self, user):
        if isinstance(user, User):
            return getattr(user, user.username)
        elif isinstance(user, Photographer):
            return getattr(user, user.pusername)

