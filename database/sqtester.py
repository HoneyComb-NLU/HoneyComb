from select import select
import sqlite3

# dbCon = sqlite3.connect("./database/database.db")
# cur = dbCon.cursor()
def coin_id_check(check_string:str):
    dbCon = sqlite3.connect('./database/database.db')
    cur = dbCon.cursor()
    
    data = cur.execute(f"""SELECT * FROM coin_list 
    WHERE id = "{check_string}" COLLATE NOCASE""").fetchall()
    
    if len(data) == 0:
        data = data = cur.execute(f"""SELECT id FROM coin_list 
        WHERE name = "{check_string}" COLLATE NOCASE""").fetchall()
    

    dbCon.commit()
    dbCon.close()
    return str(data[0][0])

def test():
    dbCon = sqlite3.connect('./database/database.db')
    cur = dbCon.cursor()
    
    data = cur.execute(f"""SELECT * FROM coin_list""").fetchall()
    
    c = 0
    for each in data:
        x = each[2].replace(" ","-").lower()
        y = each[0].lower()
        if x != y:
            c += 1
            print(each)

    print(c)
    dbCon.commit()
    dbCon.close()
    return 

# dbCon.commit()
# dbCon.close()


print(test())