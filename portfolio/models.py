from django.db import models
from django.conf import settings

class Portfolio(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='portfolio'
    )
    theme = models.CharField(max_length=50, default='default')

    def __str__(self):
        return f"{self.user.username}'s Portfolio"

class CaseStudy(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        related_name='case_studies',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    overview = models.TextField()
    media_gallery = models.JSONField(default=list, blank=True)
    timeline = models.TextField()
    tools_used = models.CharField(max_length=255)
    outcomes = models.TextField()
    slug = models.SlugField()

    class Meta:
        unique_together = ('portfolio', 'slug')

    def __str__(self):
        return f"{self.title} ({self.portfolio.user.username})"
