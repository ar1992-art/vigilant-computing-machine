# backend/portfolio/serializers.py

from rest_framework import serializers
from .models import Portfolio, CaseStudy

class CaseStudySerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(
        source='portfolio.user.username',
        read_only=True
    )

    class Meta:
        model = CaseStudy
        fields = [
            'id','title','slug','overview',
            'media_gallery','timeline','tools_used',
            'outcomes','portfolio','owner_username'
        ]
        extra_kwargs = {'portfolio': {'read_only': True}}

class PortfolioSerializer(serializers.ModelSerializer):
    case_studies = CaseStudySerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = ['user', 'theme', 'case_studies']
