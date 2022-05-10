from gensim.test.utils import common_texts, common_corpus
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel

model_path = "../../../model/lda_update.model"
model = LdaModel.load(model_path)
# print the topics
for i in range(10):
    print(model.print_topic(i))

# infer new document
new_doc = [
    ['computer', 'time', 'graph'],
    ['survey', 'response', 'eps'],
    ['human', 'system', 'computer']
]
common_dictionary = Dictionary(common_texts)
other_corpus = [common_dictionary.doc2bow(text) for text in new_doc]
unseen_doc = other_corpus[0]
vector = model[unseen_doc]
print(vector)