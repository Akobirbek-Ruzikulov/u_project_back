from rest_framework import serializers
from .models import Category, SubCategory, Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ["id", "name", "category", "prices"]


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "subcategories"]
