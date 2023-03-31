import requests
import json
import os

f = open('../tokens/auth_tokens.json', encoding='utf8')
token = f.read()
token = json.loads(token)
access_token = token['access_token']
areas = [1342, 1424, 1261, 1817, 1463, 1169, 1575, 1553, 1434, 1471, 1505, 1704, 1783, 1905, 1146, 1124, 1020, 1661,
         1932, 1061, 1890, 1475, 1422, 1041, 1646, 1255, 1586, 1347, 1530, 1438, 1975, 1174, 1217, 1103, 1614, 1500,
         1754, 1596, 1229, 1982, 1948, 1806, 1317, 1828, 1880, 1620, 1844, 1187, 1249, 1368, 1563, 1556, 1941, 1739,
         1192, 1118, 1008, 1859, 1216, 1652, 1913, 1511, 1946, 1308, 1960, 1716, 1481, 1771, 1077, 1051, 1679, 1384,
         1985, 1414, 1898, 2114, 1090, 1943]
areas = [113]

def get_page(page=0):
    params = [
        ('text', 'numerical OR semiconductor OR optics'),
        ('text.field', 'experience'),
        ('text.logic', 'all'),
        ('text.period', 'all_time'),

        ('experience', ['between1And3', 'between3And6', 'moreThan6']),
        ('education_level', ['higher', 'bachelor', 'master', 'candidate', 'doctor']),
        ('area', areas),
        ('relocation', 'living_or_relocation'),
        ('date_from', '2022-07-01'),
        ('date_to', '2022-07-09'),
        ('label', 'exclude_viewed_by_user_id'),

        ('page', page),  # Индекс страницы поиска на HH
        ('per_page', 100)  # Кол-во вакансий на 1 странице
    ]

    headers = {
        'Authorization': f'Bearer {access_token}',
             }

    req = requests.get('https://api.hh.ru/resumes', params=params, headers=headers, verify=False)
    data = req.content.decode()
    print(data)
    req.close()
    return data


def save_pages():
    for page in range(0, 20):
        jsObj = json.loads(get_page(page))
        nextFileName = '../docs/candidate_list_json/{}.json'.format(len(os.listdir('../docs/candidate_list_json')))

        f = open(nextFileName, mode='w', encoding='utf8')
        f.write(json.dumps(jsObj, ensure_ascii=False))
        f.close()

        if (jsObj['pages'] - page) <= 1:
            break

    print('Старницы поиска собраны')


save_pages()
