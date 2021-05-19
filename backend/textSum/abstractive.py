from .similaritySum import sentence_similarity_summarizer
from transformers import pipeline
from transformers import T5ForConditionalGeneration, T5Tokenizer
from transformers import GPT2Tokenizer, GPT2LMHeadModel


def hugging_face_summarizer(text):
    summarization = pipeline("summarization")

    top_k_sentences = sentence_similarity_summarizer(text).split(". ")

    summary = ""
    part_summary = ""
    numTokens = 0
    text = ""
    for sentence in top_k_sentences:
        sentTokens = len(sentence)
        print(numTokens)
        if sentTokens + numTokens < 1024:
            text += sentence
            numTokens += sentTokens
        else:
            part_summary = summarization(text)[0]['summary_text']
            summary += part_summary
            numTokens = sentTokens
            text = sentence

    return text


def t5_summarizer(text):
    model = T5ForConditionalGeneration.from_pretrained("t5-base")

    tokenizer = T5Tokenizer.from_pretrained("t5-base")

    inputs = tokenizer.encode("summarize: " + text,
                              return_tensors="pt",
                              max_length=512,
                              truncation=True)

    outputs = model.generate(inputs,
                             max_length=150,
                             min_length=40,
                             length_penalty=2.0,
                             num_beams=4,
                             early_stopping=True)

    return tokenizer.decode(outputs[0])


def gpt_summarizer(text):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    model = GPT2LMHeadModel.from_pretrained('gpt2')

    inputs = tokenizer.batch_encode_plus([text],
                                         return_tensors='pt',
                                         max_length=1000)
    summary_ids = model.generate(inputs['input_ids'], early_stopping=True)

    GPT_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return GPT_summary
