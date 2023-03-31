import json
import os
import requests
import time
from tqdm import tqdm
import urllib3
from get_tokens import get_auth_tokens
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

f = open('C:/Users/awx1160901/PycharmProjects/HH_candidate_search/tokens/auth_tokens.json', encoding='utf8')
token = f.read()
token = json.loads(token)
access_token = token['access_token']

def pages_to_resumes():
    with tqdm(total=len(os.listdir('../docs/candidate_list_json'))) as pbar:
        num_resumes = 0
        for fl in os.listdir('../docs/candidate_list_json'):
            f = open('../docs/candidate_list_json/{}'.format(fl), encoding='utf8')
            jsonText = f.read()
            f.close()
            jsonObj = json.loads(jsonText)

            for v in jsonObj['items']:
                resume_id = v['id']
                headers = {
                    'Authorization': f'Bearer {access_token}',
                }
                req = requests.get(f'https://api.hh.ru/resumes/{resume_id}', headers=headers, verify=False)
                data = req.content.decode()
                req.close()

                if num_resumes == 19500:
                    num_resumes = 0
                    time.sleep(86500)

                if data.__contains__('view_limit_exceeded'):
                    print(fl)
                    time.sleep(86500)

                if data.__contains__('token-expired') or data.__contains__('Unrecognized authorization') or data.__contains__('token_expired'):
                    get_auth_tokens()
                    continue
                fileName = '../projects/add_new_resumes/{}.json'.format(v['id'])
                f = open(fileName, mode='w', encoding='utf8')
                f.write(data)
                f.close()
                num_resumes += 1
            pbar.update(1)

    print('Кандидаты собраны')

pages_to_resumes()