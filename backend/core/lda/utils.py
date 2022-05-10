from pprint import pprint
# get the model information such as top topics, average topic coherence
def get_information(model, corpus, num_topics):
    top_topics = model.top_topics(corpus) 
    pprint(top_topics)
    # Average topic coherence
    avg_topic_coherence = sum([t[1] for t in top_topics]) / num_topics
    print('Average topic coherence: %.4f.' % avg_topic_coherence)