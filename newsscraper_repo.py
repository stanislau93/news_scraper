import sqlite3

conn = 0

def initialize():
    global conn
    if conn == 0:
        conn = sqlite3.connect('news.db')

def createTable():
    c = conn.cursor()
    query = 'CREATE TABLE words (word TEXT, frequency INTEGER)'
    c.execute(query)
    conn.commit

def select(where = None, orderBy = None):
    if where is None:
        where = []
    
    c = conn.cursor()
    query = 'SELECT * FROM words'
    if hasattr(where, "__len__") and len(where) > 0:
        query += ' WHERE'
        for column,value in where:
            query += column + ' = ' + value + ' AND '
        query = query[:-5]
    if orderBy is not None:
        query += ' ORDER BY ' + orderBy + ' DESC'
    c.execute(query)
    return c.fetchall()

def truncate():
    global conn
    c = conn.cursor()    
    query = 'DELETE FROM words'
    c.execute(query)
    conn.commit()

def insert(word):
    c = conn.cursor()
    query = 'INSERT INTO words (word,frequency) VALUES (?,1)'
    c.execute(query, (word,))
    conn.commit()

def incrementFrequency(word):
    c = conn.cursor()
    frequency = getFrequency(word)[0] + 1
    query = 'UPDATE words SET frequency = ? WHERE word = ?'
    c.execute(query, (frequency, word))
    conn.commit()

def getFrequency(word):
    c = conn.cursor()    
    query = 'SELECT frequency FROM words WHERE word = ?'
    c.execute(query, (word,))
    return c.fetchone()

def closeConnection():
    conn.close()