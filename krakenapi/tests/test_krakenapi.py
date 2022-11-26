from django.test import TestCase
from rest_framework.test import APIClient

REGISTER_URL = '/api/auth/register/'
LOGIN_URL = '/api/auth/login/'
KRAKEN_API_URL_BASE = '/api/kraken/'


class KrakenApiTests(TestCase):
    """Test kraken module API"""

    def setUp(self):
        self.client = APIClient()

    def register_user(self):
        payload = {
            'username': 'testuser',
            'password': 'testpass',
            'email': 'test@gmail.com'
        }
        res = self.client.post(REGISTER_URL, payload)
        return res

    def login_user(self):
        payload = {
            'username': 'testuser',
            'password': 'testpass'
        }
        res = self.client.post(LOGIN_URL, payload)
        token = res.data['token']
        return token

    def test_get_ticker(self):
        """Test get ticker"""
        self.register_user()
        token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res = self.client.get(KRAKEN_API_URL_BASE, {'ticker': 'XBTUSD'})
        self.assertEqual(res.status_code, 200)
        self.assertIn('XXBTZUSD', res.data)
