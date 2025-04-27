from django.db import models
from portfolio.models import CaseStudy

class Analytics(models.Model):
    case_study = models.ForeignKey(
        CaseStudy,
        related_name='analytics',
        on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('case_study', 'date')
