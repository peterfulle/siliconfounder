from django.urls import path
from .views import IndexView, SiliconFoundersView, contact_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('silicon-founders/', SiliconFoundersView.as_view(), name='silicon_founders'),
    path('contact/', contact_view, name='contact'),
]