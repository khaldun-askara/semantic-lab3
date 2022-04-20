import re
import urllib.request
from pprint import pprint
import requests

wikipages = ['https://en.wikipedia.org/w/index.php?title=Success_Automobile_Manufacturing_Company&action=history', 'https://en.wikipedia.org/w/index.php?title=Deportivo_Armenio&action=history', 'https://en.wikipedia.org/w/index.php?title=Delaware_County_Daily_Times&action=history']


def get_IPs(page):
    f = urllib.request.urlopen(page).read().decode('utf-8')
    pattern = '(\d+\.\d+\.\d+\.\d+)'
    result = re.findall(pattern, f)
    return list(set(result))


def rating(IPs):
    API_KEY = '5a2d93c719104000dbe0c39b2874214d'
    rating_dic = {}
    for ip in IPs:
        print(ip)
        url = "http://api.ipstack.com/{}?access_key={}".format(ip, API_KEY)
        request = requests.get(url)
        obj = request.json()
        country_name = obj["country_name"]
        print(country_name)
        if (country_name in rating_dic):
            rating_dic[country_name] += 1
        else:
            rating_dic[country_name] = 1
    return dict(sorted(rating_dic.items(), key=lambda item: item[1], reverse=True))

for page in wikipages:
    print(page)
    ips = get_IPs(page)
    rating_dic = rating(ips)
    print (rating_dic)
