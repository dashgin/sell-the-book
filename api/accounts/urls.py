from django.urls import include, path
from dj_rest_auth.views import PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView
from .views import ConfirmEmailView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('password/reset/confirm/<slug:uidb64>/<slug:token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
