from django.contrib import admin
from .models import PhoneBrand, PhoneInspection


@admin.register(PhoneBrand)
class PhoneBrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(PhoneInspection)
class PhoneInspectionAdmin(admin.ModelAdmin):
    list_display = ['brand', 'user', 'condition', 'price_min', 'price_max', 'confidence', 'created_at']
    list_filter = ['condition']
    search_fields = ['brand']
    ordering = ['-created_at']
