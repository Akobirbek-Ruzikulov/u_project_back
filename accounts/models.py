from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active  = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Role(models.Model):
    ADMIN = "Admin"
    USER = "User"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (USER, "User"),
    ]

    name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=2
    )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.username


