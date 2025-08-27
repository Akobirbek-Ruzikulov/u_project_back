from rest_framework import serializers
from .models import Partner, Team, Portfolio
from django.contrib.auth import get_user_model



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user



class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'user', 'name', 'image', 'is_approved']
        read_only_fields = ['user', 'is_approved']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'user', 'name', 'exp', 'position', 'avatar_img']
        read_only_fields = ['user']

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'user', 'url_link', 'image', 'title', 'description']
        read_only_fields = ['user']
