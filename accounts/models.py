from django.contrib.auth.models import AbstractUser
from django.db import models


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




class Partner(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="partners/")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    exp = models.IntegerField()
    position = models.CharField(max_length=100)
    avatar_img = models.ImageField(upload_to="teams/")

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="portfolios")
    url_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="portfolio/", blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"

