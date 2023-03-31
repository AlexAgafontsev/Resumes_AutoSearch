import random
import time
from tqdm import tqdm
import requests
import ssl
import json
from tokens.Huawei_tokens import huawei_translate_token, appid
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)



def translate(text):
    headers = {
        "Content-Type": "application/json"
    }
    ssl._create_default_https_context = ssl._create_stdlib_context
    params = {
        "appid": appid,
        "token": huawei_translate_token,
        "from": "ru",
        "to": "en",
        "content": f"{text}",
        "langdetect": "0",
    }
    url = "https://api.translate.huawei.com/api/text/translate"
    req = requests.post(url, json=params, headers=headers, verify=False)
    data = req.text
    data = json.loads(data)
    while str(data['status']) != '1001':
        url = "https://api.translate.huawei.com/api/text/translate"
        req = requests.post(url, json=params, headers=headers, verify=False)
        data = req.text
        data = json.loads(data)
        print(data)
        status = data['status']
        if status == '1003':
            print(status)
            status = '1001'
            continue
        if status != '1001' and '2003':
            print(status)
        if status == '3003':
            continue
        time.sleep(random.uniform(0.0, 2.0))
    try:
        text_en = data['trans_result']
    except:
        text_en = ''
    return text_en


