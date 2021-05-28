from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from api.contact.serializers import ContactSerializer
from contact.models import Contact


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]