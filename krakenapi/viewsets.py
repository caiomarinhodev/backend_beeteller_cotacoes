from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from krakenapi.kraken_api import get_ticker


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
        except Exception as e:
            return Response({'error': str(e)})
        return Response(ticker)
