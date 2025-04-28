# backend/analytics/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum

from portfolio.models import Portfolio
from .models import Analytics

class AnalyticsSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only stats for the logged-in user's portfolio
        portfolio = Portfolio.objects.filter(user=request.user).first()
        if not portfolio or not portfolio.case_studies.exists():
            return Response({
                'total_visits': 0,
                'total_clicks': 0,
                'per_case': []
            })

        stats = Analytics.objects.filter(case_study__portfolio=portfolio)
        total_visits = stats.aggregate(Sum('views'))['views__sum'] or 0
        total_clicks = stats.aggregate(Sum('clicks'))['clicks__sum'] or 0

        per_case = (
            stats
            .values('case_study__id', 'case_study__title')
            .annotate(views=Sum('views'), clicks=Sum('clicks'))
        )

        return Response({
            'total_visits': total_visits,
            'total_clicks': total_clicks,
            'per_case': list(per_case),
        })
