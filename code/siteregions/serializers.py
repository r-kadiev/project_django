from django.db import models
from rest_framework import serializers
from .models import SiteRegion, Region, Site


class SiteRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteRegion
        fields = ('type', 'key', 'value')


class RegionSerializer(serializers.ModelSerializer):
    site_regions = SiteRegionSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ('name', 'site_regions')


class SiteSerializer(serializers.ModelSerializer):
    regions = RegionSerializer(many=True, read_only=True)

    class Meta:
        model = Site
        fields = ('domain', 'regions')
