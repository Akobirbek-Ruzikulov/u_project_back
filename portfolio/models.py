from accounts.models import BaseModel, User
from django.db import models

class Portfolio(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="portfolios")
    url_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="portfolio/", blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"

