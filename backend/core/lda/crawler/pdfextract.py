import io

import requests
from PyPDF2 import PdfFileReader
from pdfminer.high_level import extract_text
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string
from gensim.parsing.preprocessing import preprocess_string, remove_stopwords, stem_text
import gensim

def getContentPDF(url):
    r = requests.get(url)
    f = io.BytesIO(r.content)
    reader = PdfFileReader(f)
    # print(reader.getPage(10))
    pages = reader.getNumPages()
    contents = ''
    for i in range(pages):
        contents += reader.getPage(i).extractText()
    contents = remove_stopwords(contents)
    contents = preprocess_string(contents)
    return contents
    
url = 'https://www.researchgate.net/profile/Ferdinando-Samaria/publication/220611207_HMM-based_architecture_for_face_identification/links/5c670ed8299bf1e3a5abdff0/HMM-based-architecture-for-face-identification.pdf'


def getContentPDF_pdfminer(url):
    r = requests.get(url)
    f = io.BytesIO(r.content)
    text = extract_text(f)
    text = text.replace('\n',' ')
    print(text.encode())
    # # tokens = gensim.utils.tokenize(text, lower=True)
    # CUSTOM_FILTERS = [remove_stopwords, stem_text]
    # tokens = preprocess_string(" ".join(tokens), CUSTOM_FILTERS)
    contents = preprocess_string(text)
    return contents
#print(getContentPDF(url))
