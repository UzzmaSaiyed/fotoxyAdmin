from django.utils import timezone
from django.urls import get_resolver,path
from rest_framework import generics,permissions,status,viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login,logout
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
import logging
logger = logging.getLogger(__name__)

def api_list(request):
    # Get the URL resolver for the project
    resolver = get_resolver() 
    # Get all URL patterns from the project's urlpatterns
    url_patterns = [
    path('user', UserCreate.as_view(), name='Create-User'),
    path('user/<str:pk>', UserUpdateDelete.as_view(), name='Update-Delete-User'),
    path('loginu/', loginuser.as_view(), name='Login-User'),
    path('logoutu/', logoutuser.as_view(),name='Logout-User'),
    path('photographer', PhotographerCreate.as_view(), name='Create-Photographer'),
    path('user/<str:pk>', PhotographerUpdateDelete.as_view(), name='Update-Delete-Photographer'),
    path('loginp/', loginphotographer.as_view(), name='Login-Photographer'),
    path('logoutp/', logoutphotographer.as_view(), name='Logout-Photographer'),
    path('portfolio', PortfolioCreate.as_view(), name='Create-Portfolio'),
    path('portfolio/<str:pk>', PortfolioUpdateDelete.as_view(), name='Update-Delete-Portfolio'),
    path('hire', HireCreate.as_view(), name='Create-Hire'),
    path('hire/<int:pk>', HireUpdateDelete.as_view(), name='Update-Delete-Hire'),
    path('bookingform', BookingFormCreate.as_view(), name='Create-BookingForm'),
    path('bookingform/<int:pk>', BookingFormUpdateDelete.as_view(),name='Update-Delete-BookingForm'),
    path('album', AlbumCreate.as_view(), name='Create-Album'),
    path('album/<int:pk>', AlbumUpdateDelete.as_view(), name='Update-Delete-Album'),
    path('category', CategoryCreate.as_view(), name='Create-Category'),
    path('category/<int:pk>', CategoryUpdateDelete.as_view(), name='Update-Delete-Category'),
    path('notification', NotificationCreate.as_view(), name='Create-Notification'),
    path('notification/<int:pk>', NotificationUpdateDelete.as_view(), name='Update-Delete-Notification'),
    path('forgot-password/', forgot_password, name='Forgot-Password'),
    
]

    # Iterate over URL patterns and extract relevant information
    for pattern in resolver.url_patterns:
        name = getattr(pattern, 'name', None)
        route = getattr(pattern.pattern, '_route', None)
        if name and route:
            url_patterns.append({'name': name, 'pattern': route})

    # Render the API list template with the URL patterns
    return render(request, 'api_list.html', {'url_patterns': url_patterns})



# def approve_record(request, record_id):
#     record = get_object_or_404(Login, id=record_id)
#     record.approval_status = 'approved'
#     record.save()
#     return JsonResponse({'message': 'Record approved successfully'})

# def reject_record(request, record_id):
#     record = get_object_or_404(Login, id=record_id)
#     record.delete()
#     return JsonResponse({'message': 'Record rejected and deleted successfully'})


# class LoginCreate(generics.ListCreateAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer

# class LoginUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer

def index(request):
    return render(request,'pages/tables.html')

#User

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def approve_user(request, record_id):
    record = get_object_or_404(User, username=record_id)
    record.approval_status = 'approved'
    record.save()
    return JsonResponse({'message': 'Record approved successfully'})

def reject_user(request, record_id):
    record = get_object_or_404(User, username=record_id)
    record.delete()
    return JsonResponse({'message': 'Record rejected and deleted successfully'})


class loginuser(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = User.objects.filter(email=email).first()

        if user and check_password(password, user.password):
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Login successful', 'user': serializer.data}, status=status.HTTP_200_OK
            )

        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def logoutuser(request):
#     logout(request)
#     return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

class logoutuser(APIView):
    serializer_class = UserLogoutSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        # serializer =UserLogoutSerializer(data=request.data)
        user=request.user
        if user.is_anonymous:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            # refresh_token = serializer.validated_data['refresh_token']
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            # token = Token.objects.get(user)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Token.DoesNotExist:
            return Response({'error': 'Token does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

#Photographer

class PhotographerCreate(generics.ListCreateAPIView):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer

class PhotographerUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer

def approve_photographer(request, record_id):
    record = get_object_or_404(Photographer,pusername=record_id)
    record.approval_status = 'approved'
    record.save()
    return JsonResponse({'message': 'Record approved successfully'})

def reject_photographer(request, record_id):
    record = get_object_or_404(Photographer, pusername=record_id)
    record.delete()
    return JsonResponse({'message': 'Record rejected and deleted successfully'})


class loginphotographer(generics.CreateAPIView):
    serializer_class = PhotographerLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        photographer = Photographer.objects.filter(email=email).first()

        if photographer and check_password(password, photographer.password):
            refresh = RefreshToken.for_user(photographer)
            serializer = PhotographerSerializer(photographer)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Login successful', 'user': serializer.data}, status=status.HTTP_200_OK
            )

        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

# class loginphotographer(generics.CreateAPIView):
#     serializer_class = PhotographerLoginSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         email = serializer.validated_data['email']
#         password = serializer.validated_data['password']

#         photographer = Photographer.objects.filter(email=email).first()

#         if photographer and check_password(password, photographer.password):
#             refresh = RefreshToken.for_user(photographer)

#             Token.objects.update_or_create(
#                 user=photographer,
#                 defaults={
#                     'key': str(refresh.access_token),
#                 }
#             )

#             serializer = PhotographerSerializer(photographer)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'message': 'Login successful', 'user': serializer.data}, status=status.HTTP_200_OK
#             )

#         return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)




class logoutphotographer(APIView):
    serializer_class = PhotographerLogoutSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        # serializer = PhotographerLogoutSerializer(data=request.data)
        user=request.user
        if user.is_anonymous:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            # refresh_token = serializer.validated_data['refresh_token']
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            # token = Token.objects.get(user)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Token.DoesNotExist:
            return Response({'error': 'Token does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

#Portfolio

class PortfolioCreate(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

def approve_portfolio(request, record_id):
    record = get_object_or_404(Portfolio, portfolio_id=record_id)
    record.approval_status = 'approved'
    record.save()
    return JsonResponse({'message': 'Record approved successfully'})

def reject_portfolio(request, record_id):
    record = get_object_or_404(Portfolio, portfolio_id=record_id)
    record.delete()
    return JsonResponse({'message': 'Record rejected and deleted successfully'})

#Hire
class HireCreate(generics.ListCreateAPIView):
    queryset = Hire.objects.all()
    serializer_class = HireSerializer

class HireUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hire.objects.all()
    serializer_class = HireSerializer

def approve_hire(request, record_id):
    record = get_object_or_404(Hire, hire_id=record_id)
    record.approval_status = 'approved'
    record.save()
    return JsonResponse({'message': 'Record approved successfully'})

def reject_hire(request, record_id):
    record = get_object_or_404(Hire, hire_id=record_id)
    record.delete()
    return JsonResponse({'message': 'Record rejected and deleted successfully'})

#Album
class AlbumCreate(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

#BookingForm
class BookingFormCreate(generics.ListCreateAPIView):
    queryset = BookingForm.objects.all()
    serializer_class = BookingFormSerializer

class BookingFormUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingForm.objects.all()
    serializer_class = BookingFormSerializer

def approve_bookingform(request, record_id):
    record = get_object_or_404(BookingForm, booking_id=record_id)
    record.approval_status = 'approved'
    record.save()
    return JsonResponse({'message': 'Record approved successfully'})

def reject_bookingform(request, record_id):
    record = get_object_or_404(BookingForm, booking_id=record_id)
    record.delete()
    return JsonResponse({'message': 'Record rejected and deleted successfully'})

#Notification
class NotificationCreate(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

#Category
class CategoryCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#Forgot Password

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        photographer = Photographer.objects.filter(email=email).first()
        
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.username))
            reset_link = request.build_absolute_uri(f'/reset-password/{uid}/{token}/')
            send_reset_password_email(user.email, reset_link)
            return render(request, 'password_reset_email_sent.html')

        elif photographer:
            token = default_token_generator.make_token(photographer)
            uid = urlsafe_base64_encode(force_bytes(photographer.pusername))
            reset_link = request.build_absolute_uri(f'/reset-password/{uid}/{token}/')
            send_reset_password_email(photographer.email, reset_link)
            return render(request, 'password_reset_email_sent.html')

            
        # Regardless of whether the email is found or not, show a generic message to avoid revealing existence of account
        return render(request, 'password_reset_email_sent.html')
        
    return render(request, 'forgot_password.html')

def send_reset_password_email(email, reset_link):
    subject = 'Reset Your Password'
    message = render_to_string('password_reset_email.html', {'reset_link': reset_link})
    send_mail(subject, message, 'uzzu4074@gmail.com', [email])

# @login_required


# def reset_password(request, uidb64, token):
#     uid = force_text(urlsafe_base64_decode(uidb64))
#     user = User.objects.filter(pk=uid).first()  # Use filter() and first() to avoid raising an exception
#     photographer = Photographer.objects.filter(pk=uid).first()  # Assuming Photographer is your model

#     if user:
#         model_instance = user
#     elif photographer:
#         model_instance = photographer
#     else:
#         return HttpResponseBadRequest("Invalid user or photographer")  # Handle the case where neither user nor photographer is found

#     if request.method == 'POST':
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')

#         if password == confirm_password:
#             # Check if the provided password matches the user's current hashed password
#             if check_password(confirm_password, model_instance.password):
#                 return HttpResponseBadRequest("New password should be different from the current password.")
#             else:
#                 # Proceed with setting the new password
#                 model_instance.set_password(password)
#                 model_instance.save()
#                 return redirect('password_reset_done')
#         else:
#             return HttpResponseBadRequest("Passwords don't match")
#     return render(request, 'reset_password.html')


def reset_password(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(username=uid).first()  # Assuming username is used as the ID
    photographer = Photographer.objects.filter(pusername=uid).first()

    if user:
        model_instance = user
    elif photographer:
        model_instance = photographer
    else:
        return HttpResponseBadRequest("Invalid user or photographer")

    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not password or not confirm_password:
            return HttpResponseBadRequest("Password fields cannot be empty")

        if password != confirm_password:
            return HttpResponseBadRequest("Passwords don't match")

        # Check if the new password is different from the current password
        if check_password(password,model_instance.password):
            return HttpResponseBadRequest("New password should be different from the current password.")

        # Set the new password and save the model instance
        model_instance.updatepassword(password)
        model_instance.save()
        # logger.debug(f"Password: {password}, Hashed Password: {model_instance.password}")

        return redirect('password_reset_done')

    return render(request, 'reset_password.html')

def password_reset_done_view(request):
    return render(request, 'password_reset_done.html')

