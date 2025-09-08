from django.db import models
from accounts.models import BaseModel


class News(BaseModel):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to="news/images/")
    content = models.TextField()
    content_image = models.ImageField(upload_to="news/content_images/", null=True, blank=True)
    content_video = models.FileField(upload_to="news/videos/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
