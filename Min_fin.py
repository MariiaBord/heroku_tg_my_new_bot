
#import requests для получение ответа с сайта и сохранения текст html страницы
#from bs4 import BeautifulSoup #для парсинга полученного текста html страницы

import requests


def get_htm(url):
    resp=requests.get(url,timeout=5)#Response [200] -не забанили
    res_json = resp.json()
    return res_json
    # [{"date": "2019-02-09", "bankName": "\u041e\u0422\u041f \u0411\u0430\u043d\u043a",
    #   "sourceUrl": "http:\/\/bank-ua.com\/banks\/otpbank\/", "codeNumeric": "978", "codeAlpha": "EUR",
    #   "rateBuy": "30.3000", "rateBuyDelta": 0, "rateSale": "30.9500", "rateSaleDelta": 0},
    #  {"date": "2019-02-09", "bankName": "\u041e\u0422\u041f \u0411\u0430\u043d\u043a",
    #   "sourceUrl": "http:\/\/bank-ua.com\/banks\/otpbank\/", "codeNumeric": "840", "codeAlpha": "USD",
    #   "rateBuy": "26.9000", "rateBuyDelta": 0, "rateSale": "27.2000", "rateSaleDelta": 0},]

def get_pages(res_json,current):
    data_current={}
    for ad in res_json:
        if ad['codeAlpha']==current:
            data = ad['date']
            bank=ad['bankName']
            rate_Buy = ad['rateBuy']
            rate_Sale = ad['rateSale']
            data_current.setdefault(bank, {'Buy':rate_Buy,'Sale':rate_Sale})
    return data_current

def main(command):

    current=command[1:].upper()

    url='http://bank-ua.com/export/exchange_rate_cash.json'
    result=get_pages(get_htm(url),current)
    return result



if __name__=='__main__':
    main(command='/USD')
