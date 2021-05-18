from .evaluate import summary_evaluation
from .nltkSum import nltk_summarizer
from .sumySum import *


def similarityMatrix(text):
    return text


def huggingFace(text):
    return text


def gpt(text):
    return text


def t5Model(text):
    return text


def summarize(text, summaryType):
    summarizedText = text
    if summaryType == "similarityMatrix":
        summarizedText = similarityMatrix(text)
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
        summarizedText = huggingFace(text)
    elif summaryType == "gpt":
        summarizedText = gpt(text)
    elif summaryType == "t5":
        summarizedText = t5Model(text)

    scores = summary_evaluation(text, summarizedText, human_summary=None)

    return summarizedText, scores
