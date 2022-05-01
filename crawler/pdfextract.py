import io

import requests
from PyPDF2 import PdfFileReader


def getContentPDF(url):
    r = requests.get(url)
    f = io.BytesIO(r.content)
    reader = PdfFileReader(f)
    # print(reader.getPage(10))
    pages = reader.getNumPages()
    contents = ''
    for i in range(pages):
        contents += reader.getPage(i).extractText()
    return contents.split('\n')
    
url = 'https://www.researchgate.net/profile/Ferdinando-Samaria/publication/220611207_HMM-based_architecture_for_face_identification/links/5c670ed8299bf1e3a5abdff0/HMM-based-architecture-for-face-identification.pdf'

print(getContentPDF(url))
