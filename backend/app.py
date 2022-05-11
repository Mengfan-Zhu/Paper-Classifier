from flask import Flask, request
from gensim.test.utils import common_texts, common_corpus
from gensim import corpora
from gensim.models import LdaModel
from crawler.pdfextract import getContentPDF,get_titles_links
from gensim.models import Phrases, LdaModel
from collections import defaultdict
model_path = "../model/lda_update.model"
model = LdaModel.load(model_path)
# print the topics
# for i in range(10):
#     print(model.print_topic(i))
topics = {0:'classifier using hmm',1:'clustering for classification',2:'neuron cell study',3:'hidden layer in image recognition',4:'optimize dynamic trajectory',5:'image filter',6:'RNN model in NLP',7:'other',8:'guassian approximation',9:'mean field, boltzmann and attention mechanism'}
# url = 'https://www.researchgate.net/profile/Ferdinando-Samaria/publication/220611207_HMM-based_architecture_for_face_identification/links/5c670ed8299bf1e3a5abdff0/HMM-based-architecture-for-face-identification.pdf'
# infer new document
def infer(paper):
    new_doc = [
        paper
    ]
    dictionary = corpora.Dictionary.load("../model/nips.dict")
    other_corpus = [dictionary.doc2bow(text) for text in new_doc]
    unseen_doc = other_corpus[0]
    vector = model[unseen_doc]
    topic = vector[0][0]
    prob = vector[0][1]
    for i in vector:
        if i[1] > prob:
            prob = i[1]
            topic = i[0]
    return topics[topic]
app = Flask(__name__)
ERROR = "No URL Found"
# route config
@app.route('/backend/classifier', methods=['POST'])
def classifier():
    body = request.data
    print(body)
    url = ''
    if not body:
        return ERROR
    else:
        url = body
    res = defaultdict(list)
    papers = get_titles_links(url,debug=True)
    for key,val in papers.items():
        res[infer(val)].append(key)
    return res