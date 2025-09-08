from django.db import models
from accounts.models import BaseModel, User


class Team(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    exp = models.IntegerField()
    position = models.CharField(max_length=100)
    avatar_img = models.ImageField(upload_to="teams/")

    def __str__(self):
        return self.name