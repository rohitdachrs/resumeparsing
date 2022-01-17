"""
Objective: The main objective is to create a resume parser to extract all the details of the candidate and integrate
it with the API's which are already created:

Details to be Extracted:
1. Extract Name.
2. Extract Mobile Number.
3. Extract Email Address.
4. Extract Linkedin URL (If present).
5. Extract Skills.
6. Extract Education.
7. Extract Github URL (If Present).
8. Extract Projects.

## Libraries Used:
1. NLTK
2. Spacy
3. pdfminer
4. pyresparser
5. resume-parser
6. docx2txt
7. IO
8. re
"""

## Importing necessary Libraries
import nltk
import re
import spacy
from pdfminer.high_level import extract_text_to_fp
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pyresparser import ResumeParser
from resume_parser import resumeparse
from nltk.tokenize import sent_tokenize,word_tokenize
from warnings import filterwarnings
filterwarnings('ignore')



##NLTK Download
nltk.download('punkt')
nltk.download('words')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
#nltk.download('all')
spacy.load('en_core_web_sm')

## Text Extraction from a PDF Document
def pdf2text(file_name,output_file_name):
    output_string = StringIO()
    with open(f'{file_name}','rb') as actual:
        parser = PDFParser(actual)
        doc = PDFDocument(parser)
        resrcmgr = PDFResourceManager()
        device = TextConverter(resrcmgr,output_string,laparams=LAParams())
        interpreter = PDFPageInterpreter(resrcmgr,device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        text = output_string.getvalue()
        text=text.encode('utf-8')
        file=open(f'{output_file_name}'+'.txt','wb')
        file.write(text)    
        file.close()

def extract_name(file):
    name = ResumeParser(file).get_extracted_data()['name']
    return name

def extract_mobile_no(file):
    mobile_no = ResumeParser(file).get_extracted_data()['mobile_number']
    return mobile_no

def extract_emailaddress(file):
    email_address = ResumeParser(file).get_extracted_data()['email']
    return email_address

def extract_skills(file):
    skills = ResumeParser(file).get_extracted_data()['skills']
    return skills

RESERVED_WORDS = [
    'school',
    'college',
    'university',
    'academy',
    'faculty',
    'institute',
    'faculdades',
    'Schola',
    'schule',
    'lise',
    'lyceum',
    'lycee',
    'polytechnic',
    'kolej',
    'ünivers',
    'okul',
    'Deemed',
    'College',
]

def extract_university(input_text):
    organizations = []

    # first get all the organization names using nltk
    for sent in sent_tokenize(input_text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'ORGANIZATION':
                organizations.append(' '.join(c[0] for c in chunk.leaves()))

    # we search for each bigram and trigram for reserved words
    # (college, university etc...)
    university = set()
    for org in organizations:
        for word in RESERVED_WORDS:
            if org.lower().find(word) >= 0:
                university.add(org)

    return university


    

if __name__ == '__main__':
    file_name = "/Users/rohitsanam/Downloads/AIERECSOFT/sample resumes/Anil’s resume-3.pdf"
    file= 'anil'
    pdf2text(file_name,file)
    with open('anil.txt') as f:
        lines = f.readlines()
    text = str(lines)
    
    name = extract_name(file_name)
    print(name)
    
    mobile_no = extract_mobile_no(file_name)
    print(mobile_no)
    
    
    email_address = extract_emailaddress(file_name)
    print(email_address)
    
    
    skills = extract_skills(file_name)
    print(skills)
    
    university = extract_university(text)
    print(university)
    
