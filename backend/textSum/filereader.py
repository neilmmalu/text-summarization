import textract
import webvtt
from collections import defaultdict

extensions = {
    'csv', 'doc', 'docx', 'eml', 'epub', 'gif', 'jpeg', 'jpg', 'json', ' log',
    'mp3', 'msg', 'odt', 'ogg', 'pdf', 'png', 'pptx', 'ps', 'psv', 'rtf',
    'tff', 'tif', 'tiff', 'tsv', 'txt', 'wav', 'xls', 'xlsx'
}


def getFileName(path):
    return path.split('/')[-1]


def getFileExtension(fileName):
    return fileName.split('.')[-1]


def readWebVTT(path):
    d = defaultdict(list)
    for caption in webvtt.read(path):
        t = caption.text.split(":")
        if len(t) > 1:
            d[t[0]].append(t[1])
    main_speaker, content = max(d.items(), key=lambda x: len(x[1]))
    content = list(filter(lambda x: len(x.split()) >= 5, content))

    return content


def readFile(path):
    fileName = getFileName(path)
    ext = getFileExtension(fileName)
    text = ""
    if ext not in extensions:
        if ext == "htm" or ext == "html":
            # HTML reader
            pass
        if ext == "vtt":
            # WebVTT reader
            text = readWebVTT(path)
        else:
            return None
    else:
        print(ext)
        print(fileName)
        text = textract.process(path)
        print(text)
        text = text.decode('utf-8')

    return text
