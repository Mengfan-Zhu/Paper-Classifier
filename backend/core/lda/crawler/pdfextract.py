import io

import requests
from PyPDF2 import PdfFileReader
from pdfminer.high_level import extract_text
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string
from gensim.parsing.preprocessing import preprocess_string, remove_stopwords, stem_text
import gensim
import re
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
    
url = 'http://www.cs.cmu.edu/~tom/pubs/Science-ML-2015.pdf'


def getContentPDF_pdfminer(url):
    r = requests.get(url)
    f = io.BytesIO(r.content)
    text = extract_text(f)
    # print(text.encode())
    # print(text.encode())
    words = re.split(r'\W+', text)
    for idx in range(len(words)):
        words[idx] = words[idx].lower()  # Convert to lowercase.
    # Remove numbers, but not words that contain numbers.
    words = [ word for word in words if not word.isnumeric()]
    # Remove words that are only one character.
    words = [word for word in words if len(word) > 1]
    return words
#print(getContentPDF(url))
