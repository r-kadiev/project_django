from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import SiteRegion, Site, Region
from .serializers import SiteRegionSerializer, SiteSerializer, RegionSerializer




class Users(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = {
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            }
        return Response(data)


class SiteRegionView(APIView):
    def post(self, request):
        data = request.data
        response_data = {}
        for site, regions in data.items():
            site_data = {}
            for region in regions:
                site_regions = SiteRegion.objects.filter(site_id__domain=site, region_id__name=region)
                serializer = SiteRegionSerializer(site_regions, many=True)
                site_data[region] = serializer.data
            response_data[site] = site_data
        return Response(response_data)


    def get(self, request):
        response = {}
        sites = Site.objects.all()
        regions = Region.objects.all()
        for site in sites:
            reg_ser = RegionSerializer(regions, many=True)
            response[site.domain] = reg_ser.data
        return Response(response)
