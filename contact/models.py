from django.db import models
from accounts.models import BaseModel


class Contact(BaseModel):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    business = models.CharField(max_length=255)
    service = models.CharField(
        max_length=100,
        choices=[
            ('web', 'Web-dasturlash'),
            ('mobile', 'Mobil va desktop ilovalar'),
            ('telegram', 'Telegram botlar'),
            ('seo', 'SEO va Daromad Oshirish'),
            ('ai', 'Sun’iy intellekt'),
            ('website', 'Web-sayt'),
        ]
    )

    def __str__(self):
        return self.full_name
