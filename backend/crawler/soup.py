
from bs4 import BeautifulSoup as bs
import requests
import urllib.request
from bs4.element import Comment
import re
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

def tag_visible(element):
    # if element.parent.name in ['style', 'script']:
    #     return False
    # if isinstance(element, Comment):
    #     return False
    # if re.match(r"[\s\r\n]+",str(element)): 
    #     return False
    if "This" in str(element):
        return True
    return False

def init_soup(url):
    kv = {'user-agent':user_agent}
    try:
        r = requests.get(url,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        soup = bs(html,'html.parser')
        #print(soup.prettify())
    except:
        print('failed to crawl:'+str(r.status_code))
    return soup

# url = "https://ieeexplore.ieee.org/document/5947538"
# soup = init_soup(url)
# texts = soup.find_all('div')
# print(texts)