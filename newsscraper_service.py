import pandas
import news_scraper.newsscraper_repo as repo
from news_scraper.settings import *

monthTranslations = pandas.read_csv(PROJECT_DIR + 'months.csv')

def initialize():
    repo.initialize()

def upsertWord(word):
    frequency = repo.getFrequency(word)
    if not frequency:
      repo.insert(word)
    else:
       repo.incrementFrequency(word)

'''
1) strip the text from both sides
2) remove special characters specified in signs array
3) remove numbers
'''
def cleanText(text):
    text = text.strip()
    signs = [',', '.', '-', ':', ';', '!', '?', '@', '"', '«', '»', '|', '<', '>', '%', '/', '*']

    for sign in signs:
        text = text.replace(sign, "")

    for number in range(10):
        text = text.replace(str(number), "")

    return text.lower()

def splitText(text):
    text = text.split(' ')

    smallWords = [word for word in text if len(word) <= 2] 

    for smallWord in smallWords:
        text.remove(smallWord)       

    return text

def encodeToUtf8(listToEncode):
    yield [item.encode('utf8') for item in listToEncode]

def getTranslations():
    global monthTranslations      
    return monthTranslations

def parseMonth(month, encoding):
    global monthTranslations
    serie = monthTranslations[encoding]
    indexserie = monthTranslations['month']
    return indexserie[serie == month].index[0] + 1