from portfolio.models import Portfolio
from rest_framework import serializers

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'