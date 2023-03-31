import codecs

from PyPDF2 import PdfReader
import docx
import win32com.client
from .get_clean_data import clean_data
from os import path
import re
from striprtf.striprtf import rtf_to_text


def read_document(file):
    ext_name = path.splitext(file)[1]
    text = "If you see this, it is Error"
    if ext_name == '.pdf':
        text = read_pdf(file)
    if ext_name == '.docx':
        text = read_docx(file)
    if ext_name == '.rtf':
        text = read_rtf(file)
    return text



def read_pdf(file):
    resume = PdfReader(f"{file}")
    num = 0
    num_pages = len(resume.pages)
    whole_resume = [file, [], 2]
    while num_pages > num:
        page = resume.pages[num]
        text = page.extractText()
        whole_resume[1] += clean_data(text)
        num += 1
    return whole_resume


def read_docx(file):
    resume = docx.Document(f"{file}")
    whole_resume = [file, [], 2]
    all_paras = resume.paragraphs
    for paragraph in all_paras:
        text = paragraph.text
        if text == "":
            continue
        whole_resume[1] += clean_data(text)
    return whole_resume


def read_rtf(file):
    whole_resume = [file, [], 2]
    with open(f"{file}") as infile:
        content = infile.read()
        text = rtf_to_text(content, errors="ignore")
        whole_resume[1] += clean_data(text)
    return whole_resume





#def read_doc(file):
#    word = win32com.client.Dispatch("Word.Application")
#    word.visible = False
#    wb = word.Documents.Open(f"C:\\Users\\awx1160901\\PycharmProjects\\HH_candidate_search\\docs\\agree_resumes\\{file}")
#    doc = word.ActiveDocument
#    content = doc.content
#    wb.close()
#    doc.close()
#    print(content)
#    return doc