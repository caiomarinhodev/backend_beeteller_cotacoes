from django.urls import path

from krakenapi.viewsets import TickerView

urlpatterns = []

urlpatterns += [
    path('', TickerView.as_view()),
]
