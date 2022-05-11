import io

import requests
from PyPDF2 import PdfFileReader
from pdfminer.high_level import extract_text
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string
from gensim.parsing.preprocessing import preprocess_string, remove_stopwords, stem_text
from crawler.soup import init_soup
import gensim
import re
def getContentPDF(url, debug=False):
    if debug:
        print('getting', url)
    if '.pdf' not in url and '/pdf' not in url and '.PDF' not in url:
        return None
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

def getContentPDF_pdfminer(url):
    if '.pdf' not in url and '/pdf' not in url and '.PDF' not in url:
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

def get_titles_links(url, debug=False):
    page = init_soup(url)
    titles_elems = page.find_all("a", attrs={'id':True, 'href':True, 'data-clk': True})
    titles = []
    links = []
    
    # {"id", "href","data-clk"}
    for title in titles_elems:
        titles.append(title.text)
        id = title['data-clk-atid']
        paper = page.find('a', attrs={'data-clk-atid':id })
        links.append(paper['href'])
    dic = {}
    for i in range(len(titles)):
        words = getContentPDF(links[i], debug=debug)
        if words == None:
            words = titles[i].split(' ')
        dic[titles[i]] = words
    return dic