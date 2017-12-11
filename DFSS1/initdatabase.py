import sqlite3 as db

DATABASE = "Database/directories.db"
con = db.connect(DATABASE)
with con:
    cur = con.cursor()
    cur.execute('INSERT INTO Servers (Server, Port) VALUES ("0.0.0.0", 7001)')
    cur.execute('INSERT INTO Servers (Server, Port) VALUES ("0.0.0.0", 7002)')
    con.commit()
    cur.close()