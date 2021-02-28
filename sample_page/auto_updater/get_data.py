from requests_html import HTMLSession
from bitcoin.serializers import InfoSerializer


def get_price():
    session = HTMLSession()
    url = "https://www.coindesk.com/price/bitcoin"
    print("hello")

    request = session.get(url)

    price = request.html.find('.price-large')[0].text
    marketCap = request.html.find('.price-medium')[0].text

    result = {
        "price": price,
        "marketCap": marketCap
    }

    serializer = InfoSerializer(data=result)
    if serializer.is_valid():
        print("hello")
        serializer.save()
    else:
        pass
