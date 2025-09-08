from django.db import models
from accounts.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class Price(BaseModel):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="prices")
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    is_favorite = models.BooleanField(default=False)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.price}"
