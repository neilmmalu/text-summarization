from .evaluate import summary_evaluation


def huggingFace(text):
    return text


def similarityMatrix(text):
    return text


def klSummarizer(text):
    return text


def summarize(text, summaryType):

    summarized_text = huggingFace(text)

    scores = summary_evaluation(text, summarized_text, human_summary=None)

    return summarized_text, scores
