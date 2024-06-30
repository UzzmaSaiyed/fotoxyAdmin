from django.urls import *
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView



urlpatterns = [
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('a/', index,name="Dashboard"),
    path('', api_list),
    # path('login', LoginCreate.as_view()),
    # path('l/<str:pk>', LoginUpdateDelete.as_view()),
    # path('l/<str:record_id>/approve/', approve_record, name='approve-record'),
    # path('l/<str:record_id>/reject/', reject_record, name='reject-record'),

    #User
    path('user', UserCreate.as_view()),
    path('user/<str:pk>', UserUpdateDelete.as_view()),
    path('user/<str:record_id>/approve/', approve_user, name='approve-user'),
    path('user/<str:record_id>/reject/', reject_user, name='reject-user'),
    path('loginu/', loginuser.as_view()),
    path('logoutu/', logoutuser.as_view(), name='logout'),
    # curl -X POST http://localhost:8001/logoutp/
    # curl \ -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \http://localhost:8001/loginp/logputp/

    # write above command in url page to check logout successful or not

    #Photographer
    path('photographer', PhotographerCreate.as_view()),
    path('photographer/<str:pk>', PhotographerUpdateDelete.as_view()),
    path('photographer/<str:record_id>/approve/', approve_photographer, name='approve-photographer'),
    path('photographer/<str:record_id>/reject/', reject_photographer, name='reject-photographer'),
    path('loginp/', loginphotographer.as_view()),
    path('logoutp/', logoutphotographer.as_view(), name='Logout-Photographer'),

    #Portfolio
    path('portfolio', PortfolioCreate.as_view()),
    path('portfolio/<str:pk>', PortfolioUpdateDelete.as_view()),
    path('portfolio/<int:record_id>/approve/', approve_portfolio, name='approve-portfolio'),
    path('portfolio/<int:record_id>/reject/', reject_portfolio, name='reject-portfolio'),
    #Hire
    path('hire', HireCreate.as_view()),
    path('hire/<str:pk>', HireUpdateDelete.as_view()),
    path('hire/<int:record_id>/approve/', approve_hire, name='approve-hire'),
    path('hire/<int:record_id>/reject/', reject_hire, name='reject-hire'),
    #BookingForm
    path('bookingform', BookingFormCreate.as_view()),
    path('bookingform/<str:pk>', BookingFormUpdateDelete.as_view()),
    path('bookingform/<int:record_id>/approve/', approve_bookingform, name='approve-bookingform'),
    path('bookingform/<int:record_id>/reject/', reject_bookingform, name='reject-bookingform'),
    #Album
    path('album', AlbumCreate.as_view()),
    path('album/<str:pk>', AlbumUpdateDelete.as_view()),
    #Category
    path('category', CategoryCreate.as_view()),
    path('category/<str:pk>', CategoryUpdateDelete.as_view()),
    #Notification
    path('notification', NotificationCreate.as_view()),
    path('notification/<str:pk>', NotificationUpdateDelete.as_view()),
    #taken pks of rest as str so that it runs on apiview
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', reset_password, name='reset_password'),
    path('password-reset-done/', password_reset_done_view, name='password_reset_done'),





]

# router = DefaultRouter()
# router.register('logoutp/', logoutphotographer, basename='Logout-Photographer')
# urlpatterns+=router.urls