import newsscraper_repo as repo
import newsscraper_service as service

def incrementFrequencyTest():
    repo.initialize()
    repo.truncate()
    repo.insert('test')
    repo.incrementFrequency('test')
    repo.incrementFrequency('test')
    repo.incrementFrequency('test')
    for row in repo.select():
        print (row)
    repo.closeConnection()

def cleanTextTest():
    text = ' this is a11 22 , sample text with AAAA a lot of .useless! information?'
    text = service.cleanText(text)
    text = service.splitText(text)
    print (text)

def selectTest():
    repo.initialize()
    for row in repo.select(None, 'frequency'):
        print(row)
    repo.closeConnection()

def truncateTest():
    repo.initialize()
    repo.truncate()
    repo.closeConnection()

def getFrequencyTest():
    repo.initialize()
    print(repo.getFrequency('Путин'))
    repo.closeConnection()

#truncateTest()
cleanTextTest()