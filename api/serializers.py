from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

class PhotographerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class PhotographerLogoutSerializer(serializers.Serializer):
    pass

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UserLogoutSerializer(serializers.Serializer):
    pass

    # email = serializers.CharField()

# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Login
#         fields = '__all__'
#         extra_kwargs = {'password': {'write_only': True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographer
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

# class TokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Token
#         fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class HireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hire
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookingFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingForm
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

