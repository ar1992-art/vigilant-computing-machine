from rest_framework.routers import DefaultRouter




from django.urls import path
from .views import AnalyticsSummaryView

urlpatterns = [
    # existing router URLs…
    path('summary/', AnalyticsSummaryView.as_view(), name='summary'),
]
