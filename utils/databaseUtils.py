import sqlite3
import utils.osUtils as osu

def get_nlu_channels():
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()
    nlu_channels = [each[0] for each in cur.execute("""SELECT nlu_channel_id FROM guilds""").fetchall()]
    dbCon.commit()
    dbCon.close()
    return nlu_channels

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