from pprint import pprint
import requests


def toRUB(sum, currency):
    # API_KEY = '2fa857bf65eaa4c1c003a9ddb9d629e9'
    # url = 'https://api.exchangeratesapi.io/v1/latest?access_key={}'.format(
    #     API_KEY)
    # request = requests.get(url).json()
    # return request
    if (currency == 'USD'):
        return sum*80.55
    if (currency == 'EUR'):
        return sum*87.14
    return sum


def get_salary(area, name):
    url = 'https://api.hh.ru/vacancies?text=Python&only_with_salary=true&area={}'
    request = requests.get(url.format(area)).json()
    sum = 0
    count = 0
    for item in request['items']:
        # print(item)
        if (item['salary']['from'] is not None):
            sum += toRUB(item['salary']['from'], item['salary']['currency'])
            # print(item['salary']['currency'])
        else:
            sum += toRUB(item['salary']['to'], item['salary']['currency'])
            # print(item['salary']['currency'])
        count += 1
    print('Средняя зарплата программиста на Python в городе {} составила {} рублей.'.format(
        name, sum / count))


get_salary(72, 'Пермь')
get_salary(96, 'Ижевск')
get_salary(3, 'Екатеринбург')
get_salary(1, 'Москва')
get_salary(2, 'Санкт-Петербург')
