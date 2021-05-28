from django.urls import path, include

from .views import ProfileView, ProfileSettingsView, AccountDeleteView, LoginSignupView

urlpatterns = [
    path('', include('allauth.urls')),
    path('login_signup/', LoginSignupView.as_view(), name="ls"),
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile"),
    path('profile/<int:pk>/settings/', ProfileSettingsView.as_view(), name="profile-settings"),
    path('profile/<int:pk>/settings/delete/', AccountDeleteView.as_view(), name='account-delete')
]
