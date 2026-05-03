from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class PhoneBrand(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Phone Brand'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Phone Brand')
        verbose_name_plural = _('Phone Brands')


class PhoneInspection(models.Model):
    CONDITION_CHOICES = [
        ('new',  _('New / Like New')),
        ('good', _('Good')),
        ('fair', _('Fair')),
        ('poor', _('Poor')),
    ]

    brand     = models.CharField(max_length=100, verbose_name=_('Phone Brand'))
    user      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    image     = models.ImageField(upload_to='phones/', verbose_name=_('Photo'))
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='good', verbose_name=_('Device Condition'))
    result    = models.TextField(blank=True)
    price_min = models.IntegerField(default=0)
    price_max = models.IntegerField(default=0)
    confidence = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} — {self.user}"

    class Meta:
        verbose_name = _('Phone Inspection')
        verbose_name_plural = _('Phone Inspections')
        ordering = ['-created_at']
