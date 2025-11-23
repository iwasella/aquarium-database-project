import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score);")
data = [('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)]
cur.executemany("INSERT INTO movie VALUES(?,?,?)", data)
con.commit()

res=cur.execute("SELECT * FROM movie;")
for item in res.fetchall():
    print(item)

con.close()