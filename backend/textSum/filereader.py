import textract

extensions = {
    '.csv', '.doc', '.docx', '.eml', '.epub', '.gif', '.jpeg', '.jpg', '.json',
    ' .log', '.mp3', '.msg', '.odt', '.ogg', '.pdf', '.png', '.pptx', '.ps',
    '.psv', '.rtf', '.tff', '.tif', '.tiff', '.tsv', '.txt', '.wav', '.xls',
    '.xlsx'
}


def getFileName(path):
    return path.split('/')[-1]


def getFileExtension(fileName):
    return fileName.split('.')[-1]


def cleanText(text, ext):
    # Clean the text based on extension
    return text


def readFile(path):
    fileName = getFileName(path)

    ext = getFileExtension(fileName)

    if ext not in extensions:
        if ext == "htm" or ext == "html":
            # HTML reader
            pass
        if ext == "vtt":
            # WebVTT reader
            pass
        else:
            return None
    else:
        text = textract(path)
        text = text.decode('utf-8')

    cleanedText = cleanText(text, ext)
