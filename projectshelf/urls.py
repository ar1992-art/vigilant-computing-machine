from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# SimpleJWT views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Custom auth views
from users.views import RegisterView, UserMeView

# DRF router for your apps
from rest_framework.routers import DefaultRouter
from portfolio.views import PortfolioViewSet, CaseStudyViewSet

router = DefaultRouter()
router.register(r'portfolio', PortfolioViewSet, basename='portfolio')
router.register(r'case-studies', CaseStudyViewSet, basename='case-study')
# router.register(r'analytics', AnalyticsViewSet, basename='analytics')

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT login / refresh
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    

    # Registration & current-user
    path('api/auth/register/', RegisterView.as_view(), name='auth_register'),
    path('api/auth/me/', UserMeView.as_view(), name='auth_me'),

    # Your API
    path('api/analytics/', include('analytics.urls')),  # includes summary/
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
