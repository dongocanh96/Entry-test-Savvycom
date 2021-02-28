from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Info

from .serializers import InfoSerializer


class BitcoinPriceList(APIView):
    def get(self, request):
        infos = Info.objects.all().reverse()[:10]
        data = InfoSerializer(infos, many=True).data
        return Response(data)


class LastestPrice(APIView):
    def get(self, request):
        lastest = Info.objects.last()
        data = InfoSerializer(lastest).data
        return Response(data)
        
