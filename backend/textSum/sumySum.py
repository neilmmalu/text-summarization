import sumy
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def lsa_summarizer(text):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    lsa_summarizer = LsaSummarizer()
    lsa_summary = lsa_summarizer(parser.document, 10)
    lsa_summary_text = ''
    for sentence in lsa_summary:
        lsa_summary_text += str(sentence)
    return lsa_summary_text


def luhn_summarizer(text):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    luhn_summarizer = LuhnSummarizer()
    luhn_summary = luhn_summarizer(parser.document, sentences_count=10)
    luhn_summary_text = ''
    for sentence in luhn_summary:

        luhn_summary_text += str(sentence)
    return luhn_summary_text


def kl_summarizer(text):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    kl_summarizer = KLSummarizer()
    kl_summary = kl_summarizer(parser.document, sentences_count=10)
    kl_summary_text = ''
    for sentence in kl_summary:
        kl_summary_text += str(sentence)
    return kl_summary_text


def lexrank_summarizer(text):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    lexrank_summarizer = LexRankSummarizer()
    lexrank_summary = lexrank_summarizer(parser.document, sentences_count=10)
    lexrank_summary_text = ''
    for sentence in lexrank_summary:
        lexrank_summary_text += str(sentence)
    return lexrank_summary_text
