
from gensim.models import LdaModel
from gensim.test.utils import common_corpus
from utils import get_information

num_topics = 10
model_save_path = "model/lda_update_with_common.model"
model = LdaModel.load("model/lda_nips.model")
model.update(common_corpus)
get_information(model, common_corpus, num_topics)
model.save(model_save_path)