import requests
import webbrowser
import json
from tokens.HH_client_tokens import client_secret, client_id


url = f'https://hh.ru/oauth/authorize?response_type=code&client_id={client_id}'
webbrowser.open_new(url)

print('введите код из ссылки(нужно нажать на ссылку и скопировать все что идет после code=)')
code = input()


def get_auth_tokens():
    params = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
    }
    req = requests.post('https://hh.ru/oauth/token', params=params, verify=False)  # Посылаем запрос к API
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    data = json.loads(data)
    # Создаем новый документ, записываем в него ответ запроса, после закрываем
    f = open('../tokens/auth_tokens.json', mode='w', encoding='utf8')
    f.write(json.dumps(data, ensure_ascii=False))
    f.close()
    print(data)
    req.close()

get_auth_tokens()