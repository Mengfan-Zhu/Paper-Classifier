from crawler.pdfextract import getContentPDF_pdfminer
from crawler.pdfextract import get_titles_links
url = 'https://arxiv.org/pdf/1603.08029.pdf%EF%BC%89'
page_url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C14&q=resnet&btnG='
dic = get_titles_links(page_url)
print(dic)