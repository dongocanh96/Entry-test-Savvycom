from django.urls import path
from .views import BitcoinPriceList, LastestPrice

urlpatterns = [
    path('list', BitcoinPriceList.as_view(), name='prices'),
    path('list/lastest', LastestPrice.as_view(), name='lastest')
]