from django.urls import path

from awesomeapi.viewsets import TickerView, GetAllTickersView, TickerHistoryView, GetAllAvailableCombinationsView

urlpatterns = []

urlpatterns += [
    path('', TickerView.as_view()),
    path('tickers/', GetAllTickersView.as_view()),
    path('history/', TickerHistoryView.as_view()),
    path('combinations/', GetAllAvailableCombinationsView.as_view()),
]
