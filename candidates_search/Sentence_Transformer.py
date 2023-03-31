from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
from statistics import mean
from tqdm import tqdm
from transformers import BertConfig, BertModel
import nltk
import pickle


# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('/Users/as.agafontsev/PycharmProjects/Resumes_AutoSearch/all-MiniLM-L6-v2')
model = BertModel.from_pretrained('/Users/as.agafontsev/PycharmProjects/Resumes_AutoSearch/all-MiniLM-L6-v2')

#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def read_df(filepath):
    print('Start reading data')
    resumes = pd.read_excel(f'{filepath}', engine='openpyxl')
    resumes = resumes.loc[resumes['sentences'] != '']
    resumes = resumes.loc[resumes['sentences'] != ' ']
    resumes['sentences'].replace('', np.nan, inplace=True)
    resumes['sentences'].replace(' ', np.nan, inplace=True)
    resumes.dropna(subset=['sentences'], inplace=True)
    print('done')
    return resumes




def get_embeddings(sentences):
    # Tokenize sentences
    encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

    # Compute token embeddings
    with torch.no_grad():
        model_output = model(**encoded_input)

    # Perform pooling
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

    # Normalize embeddings
    sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)
    return sentence_embeddings



def get_vectors(resumes, filepath = './for_test/temporary_data/resumes_cash_for_test'):
    with tqdm(total=len(resumes)) as pbar:
        for index, row in resumes.iterrows():
            try:
                sentence_vectors = get_embeddings(sentences=nltk.sent_tokenize(row['sentences']))
            except TypeError:
                continue
            resumes['sentence_vectors'] = resumes['sentence_vectors'].astype('object')
            resumes.at[index, 'sentence_vectors'] = sentence_vectors
            pbar.update(1)

    resumes.dropna(subset=['sentence_vectors'], inplace=True)
    with open(f'{filepath}', 'wb') as f:
        pickle.dump(resumes, f)
    return resumes





def get_example_vectors(example_resumes):
    for exa_resume in example_resumes:
        sentence_vectors = get_embeddings(sentences=exa_resume['sentences'])
        exa_resume['sentence_vectors'] = sentence_vectors
    return example_resumes








def get_result(example_resumes ,filename):
    print('1-запустить тестовые данные', '0-запустить реальные данные', sep='\n')
    status_test = input()
    print('1-загрузить последние сохраненные данные', '0-Начать выполнение программы заново(запускать только в случае ошибок)', sep='\n')
    status = input()
    if status == '1':
        if status_test == '1':
            with open('./for_test/temporary_data/resumes_cash_for_test', 'rb') as f:
                resumes = pickle.load(f)
        if status_test == '0':
            with open('./data/temporary_data/resumes_cash', 'rb') as f:
                resumes = pickle.load(f)
    if status == '0':
        if status_test == '1':
            data_resumes = read_df(filepath='./for_test/prepared_data/test_df.xlsx')
            resumes = get_vectors(data_resumes, filepath='./for_test/temporary_data/resumes_cash_for_test')
        if status_test == '0':
            data_resumes = read_df(filepath='./data/prepared_data/All_candidates_DF_translated.xlsx')
            resumes = get_vectors(data_resumes, filepath='./data/temporary_data/resumes_cash')
    resumes = pd.DataFrame(resumes)
    example_resumes = get_example_vectors(example_resumes)
    itog = []
    with tqdm(total=len(resumes)) as pbar:
        for index, row in resumes.iterrows():
            itog_for_resume = []
            for example_resume in example_resumes:
                itog_for_example = []
                for example_resume_vector in example_resume['sentence_vectors']:
                    itog_for_sentence = []
                    for sentence_vector in row['sentence_vectors']:
                        sent_sim = cosine_similarity(sentence_vector.reshape(1, -1), example_resume_vector.reshape(1, -1))[0][0]
                        itog_for_sentence.append(sent_sim)
                    itog_for_example.append(max(itog_for_sentence))
                itog_for_resume.append(mean(itog_for_example))
            itog_for_resume.append(max(itog_for_resume))
            itog_for_resume.append(row['url'])
            itog_for_resume.append(row['position_name'])
            itog.append(itog_for_resume)
            pbar.update(1)

    example_resumes_names = [example_resume['position_name'] for example_resume in example_resumes]
    example_resumes_names.append('itog')
    example_resumes_names.append('url')
    example_resumes_names.append('position name')
    result_sim = pd.DataFrame(itog, columns=example_resumes_names)
    result_sim = result_sim.sort_values(by='itog', ascending=False)

    for_excel = result_sim.iloc[0:100]
    for_excel.to_excel(f'./results/{filename}.xlsx')
    print(f'Готово!', 'Можешь забрать результат работы программы в папке', f'results/{filename}.xlsx', sep='\n')
    return