from gensim.test.utils import common_texts, common_corpus
from gensim import corpora
from gensim.models import LdaModel
from crawler.pdfextract import getContentPDF
from gensim.models import Phrases, LdaModel
model_path = "../../../model/lda_update.model"
model = LdaModel.load(model_path)
# print the topics
for i in range(10):
    print(model.print_topic(i))
url = 'https://www.researchgate.net/profile/Ferdinando-Samaria/publication/220611207_HMM-based_architecture_for_face_identification/links/5c670ed8299bf1e3a5abdff0/HMM-based-architecture-for-face-identification.pdf'
# infer new document
new_doc = [
    ['computer', 'time', 'graph'],
    ['survey', 'response', 'eps'],
    ['text', 'retrieval', 'advance','science','aaaa'],
]
dictionary = corpora.Dictionary.load("../../../model/nips.dict")
other_corpus = [dictionary.doc2bow(text) for text in new_doc]
print(other_corpus)
unseen_doc = other_corpus[2]
vector = model[unseen_doc]
print(vector)