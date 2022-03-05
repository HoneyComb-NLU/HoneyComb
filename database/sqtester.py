from select import select
import sqlite3

dbCon = sqlite3.connect("./database/database.db")
cur = dbCon.cursor()

coin_id = "bitcoin"

print(
    cur.execute(f"""SELECT name FROM coin_list 
    WHERE id = "{coin_id}" COLLATE NOCASE""").fetchall()
)



dbCon.commit()
dbCon.close()