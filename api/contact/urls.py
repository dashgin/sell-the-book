from django.urls import include, path
from .views import ContactCreateAPIView

urlpatterns = [
    path('', ContactCreateAPIView.as_view(), name='contact'),


]
