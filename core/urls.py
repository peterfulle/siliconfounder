from django.urls import path
from .views import SiliconFoundersView, contact_view

urlpatterns = [
    # Silicon Founders como página principal
    path('', SiliconFoundersView.as_view(), name='index'),
    path('contact/', contact_view, name='contact'),
]