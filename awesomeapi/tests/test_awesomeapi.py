from django.test import TestCase
from rest_framework.test import APIClient

REGISTER_URL = '/api/auth/register/'
LOGIN_URL = '/api/auth/login/'
AWESOME_API_URL_BASE = '/api/awesome/'
AWESOME_API_URL_BASE_HISTORY = '/api/awesome/history/'
AWESOME_API_URL_BASE_ALL_TICKERS = '/api/awesome/tickers/'
AWESOME_API_URL_BASE_ALL_COMBINATIONS = '/api/awesome/combinations/'


class AwesomeApiTests(TestCase):
    """Test awesome module API"""

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

    def test_get_all_tickers(self):
        """Test get all tickers"""
        self.register_user()
        token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res = self.client.get(AWESOME_API_URL_BASE_ALL_TICKERS)
        self.assertEqual(res.status_code, 200)
        self.assertIn('BRL', res.data)

    def test_get_all_tickers_unauthorized(self):
        """Test get all tickers unauthorized"""
        res = self.client.get(AWESOME_API_URL_BASE_ALL_TICKERS)
        self.assertEqual(res.status_code, 401)
        self.assertIn('detail', res.data)

    def test_get_all_combinations(self):
        """Test get all combinations"""
        self.register_user()
        token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res = self.client.get(AWESOME_API_URL_BASE_ALL_COMBINATIONS)
        self.assertEqual(res.status_code, 200)

    def test_get_all_combinations_unauthorized(self):
        """Test get all combinations unauthorized"""
        res = self.client.get(AWESOME_API_URL_BASE_ALL_COMBINATIONS)
        self.assertEqual(res.status_code, 401)
        self.assertIn('detail', res.data)

    def test_get_ticker(self):
        """Test get ticker"""
        self.register_user()
        token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res = self.client.get(AWESOME_API_URL_BASE, {'ticker': 'BRL-USD'})
        self.assertEqual(res.status_code, 200)
        self.assertIn('BRLUSD', res.data)

    def test_get_ticker_unauthorized(self):
        """Test get ticker unauthorized"""
        res = self.client.get(AWESOME_API_URL_BASE, {'ticker': 'BRL-USD'})
        self.assertEqual(res.status_code, 401)
        self.assertIn('detail', res.data)

    def test_get_ticker_invalid(self):
        """Test get ticker invalid"""
        self.register_user()
        token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res = self.client.get(AWESOME_API_URL_BASE, {'ticker': 'INVALID'})
        self.assertEqual(res.status_code, 200)
        self.assertIn('error', res.data)

    def test_get_ticker_history(self):
        """Test get ticker history"""
        self.register_user()
        token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res = self.client.get(AWESOME_API_URL_BASE_HISTORY, {'ticker': 'BRL-USD', 'days': 3})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 3)

    def test_get_ticker_history_unauthorized(self):
        """Test get ticker history unauthorized"""
        res = self.client.get(AWESOME_API_URL_BASE_HISTORY, {'ticker': 'BRL-USD', 'days': 3})
        self.assertEqual(res.status_code, 401)
        self.assertIn('detail', res.data)

    def test_get_ticker_history_invalid(self):
        """Test get ticker history invalid"""
        self.register_user()
        token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res = self.client.get(AWESOME_API_URL_BASE_HISTORY, {'ticker': 'INVALID', 'days': 3})
        self.assertEqual(res.status_code, 200)
        self.assertIn('error', res.data)

    def test_get_ticker_history_invalid_days(self):
        """Test get ticker history invalid days"""
        self.register_user()
        token = self.login_user()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        res = self.client.get(AWESOME_API_URL_BASE_HISTORY, {'ticker': 'BRL-USD', 'days': 'invalid'})
        self.assertEqual(res.status_code, 200)
        self.assertIn('error', res.data)
