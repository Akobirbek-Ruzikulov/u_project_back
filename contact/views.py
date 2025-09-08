from rest_framework import generics, permissions
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact
from .serializers import ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        contact = serializer.save()

        subject = "Yangi Contact form yuborildi!"
        message = (
            f"Yangi murojaat keldi:\n\n"
            f"Ism-familya: {contact.full_name}\n"
            f"Telefon: {contact.phone}\n"
            f"Biznesingiz: {contact.business}\n"
            f"Xizmat: {contact.get_service_display()}\n"
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
