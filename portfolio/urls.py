# (not strictly needed if using the main router in projectshelf/urls.py)
from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet, CaseStudyViewSet

router = DefaultRouter()
router.register(r'portfolio', PortfolioViewSet, basename='portfolio')
router.register(r'case-studies', CaseStudyViewSet, basename='case-study')

urlpatterns = router.urls
