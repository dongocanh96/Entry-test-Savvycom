from django.urls import path
from .views import BitcoinPriceList

urlpatterns = [
    path('', BitcoinPriceList.as_view(), name='bitcoin_price')
]