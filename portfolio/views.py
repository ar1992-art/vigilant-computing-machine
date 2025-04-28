# backend/portfolio/views.py

from datetime import date
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Portfolio, CaseStudy
from .serializers import PortfolioSerializer, CaseStudySerializer
from .permissions import IsOwnerOrReadOnly

from analytics.models import Analytics


class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Portfolio.objects.select_related('user').prefetch_related('case_studies')
    serializer_class = PortfolioSerializer
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'
    permission_classes = [permissions.AllowAny]


class CaseStudyViewSet(viewsets.ModelViewSet):
    """
    - Anyone can list/retrieve case studies (view).
    - Only the owner can create/update/delete.
    - Anyone can record views/clicks.
    """
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    permission_classes = [
         permissions.IsAuthenticatedOrReadOnly,
         IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        portfolio = get_object_or_404(Portfolio, user=self.request.user)
        serializer.save(portfolio=portfolio)

    @action(detail=True, methods=['post'], permission_classes=[permissions.AllowAny])
    def record_view(self, request, pk=None):
        case = self.get_object()
        analytics, _ = Analytics.objects.get_or_create(
            case_study=case,
            date=date.today()
        )
        analytics.views += 1
        analytics.save()
        return Response({'status': 'view recorded'})

    @action(detail=True, methods=['post'], permission_classes=[permissions.AllowAny])
    def record_click(self, request, pk=None):
        case = self.get_object()
        analytics, _ = Analytics.objects.get_or_create(
            case_study=case,
            date=date.today()
        )
        analytics.clicks += 1
        analytics.save()
        return Response({'status': 'click recorded'})
