import sqlite3
import utils.osUtils as osu
# import osUtils as osu

def set_def_currencies(guild_id:int, def_currency:str):
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()

    def_currency = str(def_currency).replace(" ","").lower()
    if len(cur.execute(f"""SELECT * FROM guilds WHERE guild_id = {guild_id}""").fetchall()) == 0:
        return False
    
    for e in def_currency.split(","):
        if len(supported_currency_check(e)) == 0:
            return False

    cur.execute(f"""UPDATE guilds
    SET default_vs_currency = "{def_currency}"
    WHERE guild_id = {guild_id}
    """)

    dbCon.commit()
    dbCon.close()
    return True

def get_nlu_channels():
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()
    nlu_channels = [each[0] for each in cur.execute("""SELECT nlu_channel_id FROM guilds""").fetchall()]
    dbCon.commit()
    dbCon.close()
    return nlu_channels

def check_nlu_channels(channel_id:int):
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()
    nlu_channel = cur.execute(f"""SELECT nlu_channel_id FROM guilds WHERE nlu_channel_id = "{channel_id}" """).fetchall()
    dbCon.commit()
    dbCon.close()
    return len(nlu_channel) > 0

def get_all_currencies():
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()
    currency_list = [each[0] for each in cur.execute("SELECT * from supported_currencies").fetchall()]
    # print(list(cur.execute("SELECT * from supported_currencies")))
    dbCon.commit()
    dbCon.close()
    return currency_list

def remove_guild(guild_id):
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()
    
    cur.execute(f"""DELETE FROM guilds WHERE guild_id = {guild_id}""")

    dbCon.commit()
    dbCon.close()

def coin_id_check(check_string:str):
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()
    
    data = cur.execute(f"""SELECT * FROM coin_list 
    WHERE id = "{check_string}" COLLATE NOCASE""").fetchall()

    dbCon.commit()
    dbCon.close()
    return data

def supported_currency_check(check_string:str):
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()
    
    data = cur.execute(f"""SELECT * FROM supported_currencies
    WHERE id = "{check_string}" COLLATE NOCASE""").fetchall()

    dbCon.commit()
    dbCon.close()
    return data

def search_thru_db_for(query_string:str):
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()
    
    data = cur.execute(f"""SELECT * FROM coin_list 
    WHERE id = "{query_string}" COLLATE NOCASE
    OR symbol = "{query_string}" COLLATE NOCASE
    OR name = "{query_string}" COLLATE NOCASE """).fetchall()

    dbCon.commit()
    dbCon.close()
    return data

def get_default_currency(guild_id:int):
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()
    
    def_currency = cur.execute(f"""SELECT default_vs_currency FROM guilds WHERE guild_id = {guild_id}""").fetchall()
    
    dbCon.commit()
    dbCon.close()

    return str(def_currency[0][0])

def get_coin_name(coin_id:str):
    # print(coin_id)
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()
    
    data = cur.execute(f"""SELECT name FROM coin_list 
    WHERE id = "{coin_id}" COLLATE NOCASE""").fetchall()

    dbCon.commit()
    dbCon.close()
    # print(data[0][0])
    return str(data[0][0])


