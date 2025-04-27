# backend/portfolio/serializers.py

from rest_framework import serializers
from .models import Portfolio, CaseStudy

class CaseStudySerializer(serializers.ModelSerializer):
    # Mark portfolio as read-only so DRF won't expect it on input
    class Meta:
        model = CaseStudy
        fields = '__all__'
        extra_kwargs = {
            'portfolio': {'read_only': True},
        }

class PortfolioSerializer(serializers.ModelSerializer):
    case_studies = CaseStudySerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = ['user', 'theme', 'case_studies']
