from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .awesome_api import get_all_tickers, get_ticker, get_history_ticker, get_all_available_combinations


class GetAllTickersView(APIView):
    """
    Get all tickers API endpoint.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            tickers = get_all_tickers()
            return Response(tickers)
        except Exception as e:
            return Response({'error': str(e)})


class TickerView(APIView):
    """
    Get ticker API endpoint.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        ticker = request.GET.get('ticker')
        try:
            ticker = get_ticker(ticker)
            return Response(ticker)
        except Exception as e:
            return Response({'error': str(e)})


class TickerHistoryView(APIView):
    """
    Get ticker history API endpoint.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        ticker = request.GET.get('ticker')
        days = request.GET.get('days')
        try:
            history_ticker = get_history_ticker(ticker, days)
            return Response(history_ticker)
        except Exception as e:
            return Response({'error': str(e)})


class GetAllAvailableCombinationsView(APIView):
    """
    Get all available combinations API endpoint.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            combinations = get_all_available_combinations()
            return Response(combinations)
        except Exception as e:
            return Response({'error': str(e)})
