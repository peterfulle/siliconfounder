from django.db import models
from django.contrib.auth.models import User

# Modelos existentes (mantén los que ya tienes)
class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, help_text="Nombre del ícono de Font Awesome")
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    quote = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} - {self.company}"
    
    class Meta:
        ordering = ['order']

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    technologies = models.TextField(help_text="Comma-separated list of technologies")
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']

# NUEVOS MODELOS PARA SILICON FOUNDERS
class Industry(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class FounderProfile(models.Model):
    INDUSTRY_CHOICES = [
        ('fintech', 'Fintech'),
        ('healthtech', 'HealthTech'),
        ('edtech', 'EdTech'),
        ('proptech', 'PropTech'),
        ('deeptech', 'DeepTech'),
        ('saas', 'SaaS'),
        ('ecommerce', 'E-commerce'),
        ('ai_ml', 'AI/ML'),
        ('biotech', 'Biotech'),
        ('cleantech', 'CleanTech'),
    ]
    
    FUNDING_STAGE = [
        ('pre_seed', 'Pre-Seed'),
        ('seed', 'Seed'),
        ('series_a', 'Series A'),
        ('series_b', 'Series B+'),
        ('revenue', 'Revenue Stage'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    funding_stage = models.CharField(max_length=50, choices=FUNDING_STAGE)
    country_origin = models.CharField(max_length=100)
    linkedin_url = models.URLField(blank=True)
    company_website = models.URLField(blank=True)
    pitch_deck_url = models.URLField(blank=True)
    brief_description = models.TextField(max_length=500)
    logo = models.ImageField(upload_to='founder_logos/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.company_name}"

class Event(models.Model):
    EVENT_TYPE = [
        ('networking', 'Networking Mixer'),
        ('pitch_night', 'Pitch Night'),
        ('panel', 'Panel Discussion'),
        ('workshop', 'Workshop'),
        ('breakfast', 'Founders Breakfast'),
    ]
    
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    max_attendees = models.IntegerField(default=50)
    registration_url = models.URLField(blank=True)
    featured_image = models.ImageField(upload_to='events/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']