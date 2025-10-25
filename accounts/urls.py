from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns=[
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('test/',TestAPiView.as_view(), name='test'),
    path('send-otp/', SendOtpView.as_view(), name='send-otp'),
    path('verify-otp/', verify_otp, name='generate_otp'),
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', loginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('resend-otp/', ResendOTPAPIView.as_view(), name='resend-otp'),
    path('create-agent/', AgentRegisterAPIView.as_view(), name='create agent'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('FATCA/', FatcaAPIView.as_view(), name='fatca'),
    path('mandate/', MandateAPIView.as_view(), name='mandate'),
    path('enach/', EnachAPIView.as_view(), name='enach'),
    path('XSIP/', XSIPAPIView.as_view(), name='XSIP'),
    path('AMC_list_upload/', AMCAPIView.as_view(), name="AMC list"),
    path('cart/', AMCCartAPIView.as_view(), name="cart")
]