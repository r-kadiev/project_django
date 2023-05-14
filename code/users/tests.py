from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from users.models import CustomUser


class CustomUserTestApi(APITestCase):

    def setUp(self):


        self.user = CustomUser.objects.create_user(username='user', email='test_api@test_api.py', password='TestApi1234')
        self.user_token = Token.objects.create(user=self.user).key
        self.user.save()

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_token}')

    def test_api(self):
        r = self.client.get('/users/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)