from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class Users(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = {
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            }
        return Response(data)