from .evaluate import summary_evaluation


def nltkSummarizer(text):
    return text


def similarityMatrix(text):
    return text


def lsaSummarizer(text):
    return text


def klSummarizer(text):
    return text


def luhnSummarizer(text):
    return text


def lexRankSummarizer(text):
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
        summarizedText = nltkSummarizer(text)
    elif summaryType == "lsaSummarizer":
        summarizedText = lsaSummarizer(text)
    elif summaryType == "klSummarizer":
        summarizedText = klSummarizer(text)
    elif summaryType == "luhnSummarizer":
        summarizedText = luhnSummarizer(text)
    elif summaryType == "lexRankSummarizer":
        summarizedText = lexRankSummarizer(text)
    elif summaryType == "huggingFace":
        summarizedText = huggingFace(text)
    elif summaryType == "gpt":
        summarizedText = gpt(text)
    elif summaryType == "t5":
        summarizedText = t5Model(text)

    scores = summary_evaluation(text, summarizedText, human_summary=None)

    return summarizedText, scores
