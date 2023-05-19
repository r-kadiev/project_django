from django.urls import path
from .views import SiteRegionAPIView

urlpatterns = [
    path('site-region/', SiteRegionAPIView.as_view(), name='site-region'),
]