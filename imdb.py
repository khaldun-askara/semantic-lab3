import matplotlib.pyplot as plt
import requests
from textblob import TextBlob

ids = ["tt0111161", "tt8115900", "tt18689424", "tt3794354", "tt0050083"]
API_KEY = "k_5f56ju4l"
url = 'https://imdb-api.com/API/Reviews/{}/{}'


def get_polaritys():
    reviews = []
    rate = []
    polar = []
    for id in ids:
        print(id)
        request = requests.get(url.format(API_KEY, id)).json()
        for item in request['items']:
            if (item['rate'] != ''):
                testimonial = TextBlob(item['content'])
                reviews.append((item["rate"], testimonial.sentiment.polarity))
                rate.append(item["rate"])
                polar.append(testimonial.sentiment.polarity)

    print (reviews)
    plt.scatter(polar, rate)
    plt.show()


print (get_polaritys())
# plt.plot((0, 1, 2, 3, 4, 5, 6, 7), (0, 3, 1, 2, 1, 5, 4, 0))
# plt.show()
