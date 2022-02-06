import sqlite3
import utils.osUtils as osu

def get_nlu_channels():
    dbCon = sqlite3.connect(osu.get_db())
    cur = dbCon.cursor()
    nlu_channels = [each[0] for each in cur.execute("""SELECT nlu_channel_id FROM guilds""").fetchall()]
    dbCon.commit()
    dbCon.close()
    return nlu_channels

