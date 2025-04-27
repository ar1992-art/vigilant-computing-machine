from rest_framework import viewsets, permissions
from .models import Analytics
from .serializers import AnalyticsSerializer

class AnalyticsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    GET /api/analytics/ → list metrics
    """
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
    permission_classes = [permissions.AllowAny]


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from portfolio.models import Portfolio, CaseStudy
from .models import Analytics

class AnalyticsSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 1) Find the current user's portfolio
        portfolio = Portfolio.objects.get(user=request.user)

        # 2) Aggregate total views & clicks
        stats = Analytics.objects.filter(case_study__portfolio=portfolio)
        total_visits = stats.aggregate(Sum('views'))['views__sum'] or 0
        total_clicks = stats.aggregate(Sum('clicks'))['clicks__sum'] or 0

        # 3) Per-case breakdown
        per_case = (
            stats
            .values('case_study__id', 'case_study__title')
            .annotate(views=Sum('views'), clicks=Sum('clicks'))
        )

        return Response({
            'total_visits': total_visits,
            'total_clicks': total_clicks,
            'per_case': per_case,
        })

