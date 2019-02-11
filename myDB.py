import sqlite3

db = sqlite3.connect("data/database.db")
cur = db.cursor()

def joss(sql):
    cur.execute(sql)
    db.commit()

def eksekusi(sql):
    cur.execute(sql)
    lineData = cur.fetchall()
    totData = len(lineData)
    return lineData, totData
