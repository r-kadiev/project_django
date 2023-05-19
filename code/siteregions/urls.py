from django.urls import path
from .views import SiteRegionAPIView

urlpatterns = [
    path('', SiteRegionAPIView.as_view(), name='site-region'),
]