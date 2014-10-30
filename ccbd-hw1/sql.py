import sqlite3
import string


def connect_db():
    conn = sqlite3.connect('tweets.db')
    return conn


def build(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE tweets
                     (date text, tweet text, geo text)''')
    conn.commit()


def cclose(conn):
    conn.commit()
    conn.close()


def insert(conn, date, text, geo):
    c = conn.cursor()
    #date = date.translate(string.maketrans("", ""), string.punctuation)
    text = text.translate(string.maketrans("", ""), string.punctuation)
    #geo = geo.translate(string.maketrans("", ""), string.punctuation)

    c.execute("INSERT INTO tweets VALUES (?,?,?)",
             (date, text, geo))

    conn.commit()


def get(conn, date="", text="", geo=""):
    c = conn.cursor()
    result = []
    for row in c.execute('SELECT * FROM tweets'):
        if((date is "" or date in row[0]) and
          (text is "" or text.lower() in row[1].lower()) and
          (geo is "" or geo in row[2])):
            result.append(row)
    return result


def filter(conn, text):
    results = get(conn, text=text)
    return results


def format_js(text):
    s = []
    return s
