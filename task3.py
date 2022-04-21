import requests
import re
MODEL = 'ruscorpora_upos_cbow_300_20_2019'
MODEL2 = 'tayga_upos_skipgram_300_2_2019'
FORMAT = 'csv'
WORDS = ['молоко', 'президент', 'учить', 'хороший']
def api_neighbor(m, w, f):
    neighbors = {}
    url = '/'.join(['http://rusvectores.org', m, w, 'api', f]) + '/'
    r = requests.get(url=url, stream=True)
    for line in r.text.split('\n'):
        try: # первые две строки в файле -- служебные, их мы пропустим
            word, sim = re.split('\s+', line) # разбиваем строку по одному или более пробелам
            neighbors[word] = sim
        except:
            continue
    return neighbors

def api_similarity(m, w1, w2):
    url = '/'.join(['https://rusvectores.org', m, w1 + '__' + w2, 'api', 'similarity/'])
    r = requests.get(url, stream=True)
    return r.text.split('\t')[0]

for word in WORDS:
    print(api_neighbor(MODEL, word, FORMAT))

print(api_similarity(MODEL2, 'кошка', 'собака'))
print(api_similarity(MODEL2, 'собака', 'компьютер'))