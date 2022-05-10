import io

import requests
from PyPDF2 import PdfFileReader
from pdfminer.high_level import extract_text
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string
from gensim.parsing.preprocessing import preprocess_string, remove_stopwords, stem_text
from crawler.soup import init_soup
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
    # print(text.encode())
    # print(text.encode())
    words = re.split(r'\W+', contents)
    for idx in range(len(words)):
        words[idx] = words[idx].lower()  # Convert to lowercase.
    # Remove numbers, but not words that contain numbers.
    words = [ word for word in words if not word.isnumeric()]
    # Remove words that are only one character.
    words = [word for word in words if len(word) > 1]
    return words
    
url = 'http://www.cs.cmu.edu/~tom/pubs/Science-ML-2015.pdf'


def getContentPDF_pdfminer(url):
    print(url)
    if '.pdf' not in url and '/pdf' not in url:
        return None
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

def get_titles_links(url):
    page = init_soup(url)
    titles_elems = page.findAll("a", attrs={'id':True, 'href':True, 'data-clk': True})
    papers_elems = page.findAll("a", attrs= {'id':False, 'href': True, 'data-clk': True, 'data-clk-atid':True})
    titles = []
    links = []
    
    # {"id", "href","data-clk"}
    for title in titles_elems:
        titles.append(title.text)
        print(title.text)
    for paper in papers_elems:
        links.append(paper['href'])
        print(paper['href'])
    print(len(links))
    print(len(titles))
    dic = {}
    # for i in range(len(titles)):
    #     words = getContentPDF_pdfminer(links[i])
    #     if words == None:
    #         words = titles[i].split(' ')
    #     dic[titles[i]] = words
    return dic