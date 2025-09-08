from django.db import models
from accounts.models import BaseModel, User


class Partner(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="partners/")
    site = models.URLField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name