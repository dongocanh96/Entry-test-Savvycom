from requests_html import HTMLSession
from bitcoin.serializers import InfoSerializer, InfoNopkSerializer
from bitcoin.models import Info


def get_price():
    session = HTMLSession()
    url = "https://www.coindesk.com/price/bitcoin"

    request = session.get(url)

    price = request.html.find('.price-large')[0].text
    marketCap = request.html.find('.price-medium')[0].text

    result = {
        "price": price,
        "marketCap": marketCap
    }
    lastest_price = Info.objects.last()
    lastestdata = InfoNopkSerializer(lastest_price).data
    if (lastestdata != result):
        serializer = InfoSerializer(data=result)
        if serializer.is_valid():
            serializer.save()
        else:
            pass
