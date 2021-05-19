from .evaluate import summary_evaluation
from .nltkSum import nltk_summarizer
from .sumySum import *
from .similaritySum import sentence_similarity_summarizer
from .abstractive import *


def summarize(text, summaryType):
    summarizedText = text
    print(summaryType)
    if summaryType == "similarityMatrix":
        summarizedText = sentence_similarity_summarizer(text)
    elif summaryType == "nltkSummarizer":
        summarizedText = nltk_summarizer(text)
    elif summaryType == "lsaSummarizer":
        summarizedText = lsa_summarizer(text)
    elif summaryType == "klSummarizer":
        summarizedText = kl_summarizer(text)
    elif summaryType == "luhnSummarizer":
        summarizedText = luhn_summarizer(text)
    elif summaryType == "lexRankSummarizer":
        summarizedText = lexrank_summarizer(text)
    elif summaryType == "huggingFace":
        summarizedText = hugging_face_summarizer(text)
    elif summaryType == "gpt":
        summarizedText = gpt_summarizer(text)
    elif summaryType == "t5":
        summarizedText = t5_summarizer(text)

    scores = summary_evaluation(text, summarizedText, human_summary=None)

    return summarizedText, scores
