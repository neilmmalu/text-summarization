from rouge import Rouge
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim import corpora, models, similarities
import jieba


def get_jaccard_sim(str1, str2):
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()


def get_cosine_sim(*strs):
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)


def get_gensim(generated_summary, actual_text_tosum):
    texts = actual_text_tosum
    keyword = generated_summary

    texts = [jieba.lcut(text) for text in texts]
    dictionary = corpora.Dictionary(texts)
    feature_cnt = len(dictionary.token2id)
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    kw_vector = dictionary.doc2bow(jieba.lcut(keyword))
    index = similarities.SparseMatrixSimilarity(tfidf[corpus],
                                                num_features=feature_cnt)
    sim = index[tfidf[kw_vector]]
    x = []
    for i in range(len(sim)):
        x.append(sim[i])
    return (sum(x) / len(x))


def summary_evaluation(actual_text_tosum, generated_summary, human_summary):
    jc_score, co_score, ge_score, ro_score = None, None, None, None
    if actual_text_tosum is not None:
        jc_score = get_jaccard_sim(generated_summary, actual_text_tosum)
        co_score = get_cosine_sim(generated_summary, actual_text_tosum)[0, 1]
        ge_score = get_gensim(generated_summary, actual_text_tosum)
        print("Jaccard Similarity Score:", jc_score)
        print("Cosine Similarity Score:", co_score)
        print("Gensim Score:", ge_score)

    if human_summary is not None:
        rouge = Rouge()
        ro_score = rouge.get_scores(generated_summary, human_summary, avg=True)
        print(ro_score)

    return jc_score, co_score, ge_score, ro_score
