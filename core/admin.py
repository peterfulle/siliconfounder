from django.contrib import admin
from .models import Contact, FounderProfile, Event, Industry, InvestorProfile

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    search_fields = ['name', 'email', 'subject', 'message']
    list_filter = ['read', 'created_at']
    readonly_fields = ['created_at']
    list_editable = ['read']

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'description']

@admin.register(FounderProfile)
class FounderProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'industry', 'funding_stage', 'featured', 'created_at']
    search_fields = ['company_name', 'user__first_name', 'user__last_name', 'brief_description']
    list_filter = ['industry', 'funding_stage', 'featured', 'country_origin']
    list_editable = ['featured']
    readonly_fields = ['created_at']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'date', 'location', 'featured', 'max_attendees']
    search_fields = ['title', 'description', 'location']
    list_filter = ['event_type', 'featured', 'date']
    list_editable = ['featured']
    readonly_fields = ['created_at']

@admin.register(InvestorProfile)
class InvestorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'investor_type', 'featured', 'created_at']
    search_fields = ['company_name', 'user__first_name', 'user__last_name']
    list_filter = ['investor_type', 'featured']
    list_editable = ['featured']
    readonly_fields = ['created_at']