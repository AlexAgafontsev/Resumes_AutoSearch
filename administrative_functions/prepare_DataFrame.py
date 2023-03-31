import json
import os
import time
from datetime import datetime
import xlsxwriter
from tqdm import tqdm
from administrative_functions.translate import translate
from multiprocessing import Pool
import numpy as np
workbook = xlsxwriter.Workbook(f'../data/prepared_data/candidates_trasnlated_50k.xlsx', {'strings_to_urls': False})
worksheet = workbook.add_worksheet()
worksheet.write(f'A1', 'id')
worksheet.write(f'B1', 'url')
worksheet.write(f'C1', 'age')
worksheet.write(f'D1', 'city')
worksheet.write(f'E1', 'total_experience')
worksheet.write(f'F1', 'education_level')
worksheet.write(f'G1', 'company')
worksheet.write(f'H1', 'position_name')
worksheet.write(f'I1', 'sentences')
worksheet.write(f'J1', 'start_work')
worksheet.write(f'K1', 'end_work')
worksheet.write(f'L1', 'skills_set')


directory = os.listdir('../data/resumes')



def get_experience(small_directory):
    list_of_candidates = []
    with tqdm(total=len(small_directory)) as pbar:
        for file in small_directory:
            file = f"../data/resumes/{file}"
            f = open(file, encoding='utf8')
            jsonText = f.read()
            jsonObj = json.loads(jsonText)
            candidat_id = jsonObj['id']
            url = jsonObj['alternate_url']
            age = jsonObj['age']
            city = jsonObj['area']['name']
            total_experience = jsonObj['total_experience']['months']
            education_level = jsonObj['education']['level']['id']
            skill_set = jsonObj['skill_set']
            skill_set = ', '.join(skill_set)
            experience = jsonObj['experience']
            prof_role = jsonObj['professional_roles'][0]
            for exp in experience:
                company = exp['company']
                exp_position = exp['position']
                exp_des = exp['description']
                start_work = exp['start']
                end_work = exp['end']
                if exp_des != '':
                    if len(exp_des) > 4999:
                        exp_des = ''
                    else:
                        exp_des = translate(exp_des)
                else:
                    exp_des = ''
                list_of_candidates.append([candidat_id, url, age, city, total_experience, education_level, company,
                                           exp_position, exp_des, start_work, end_work, skill_set])
            pbar.update(1)
    return list_of_candidates





if __name__ == '__main__':
    num_ex = 2
    print('Введите количество потоков')
    num_threads = int(input())
    current_datetime = datetime.now()
    print(current_datetime)
    list_of_files = np.array_split(directory, num_threads)
    with Pool(num_threads) as pool:
        for thread in pool.map(get_experience, list_of_files):
            for resume in thread:
                worksheet.write(f'A{num_ex}', resume[0])
                worksheet.write(f'B{num_ex}', resume[1])
                worksheet.write(f'C{num_ex}', resume[2])
                worksheet.write(f'D{num_ex}', resume[3])
                worksheet.write(f'E{num_ex}', resume[4])
                worksheet.write(f'F{num_ex}', resume[5])
                worksheet.write(f'G{num_ex}', resume[6])
                worksheet.write(f'H{num_ex}', resume[7])
                worksheet.write(f'I{num_ex}', resume[8])
                worksheet.write(f'J{num_ex}', resume[9])
                worksheet.write(f'K{num_ex}', resume[10])
                worksheet.write(f'L{num_ex}', resume[11])
                num_ex += 1
        workbook.close()
        current_datetime = datetime.now()
        print(current_datetime)

