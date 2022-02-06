from pycoingecko import CoinGeckoAPI
import sqlite3
import discord 
import utils.consoleLogger as log
import utils.osUtils as osu

db_url = osu.get_db()
# db_url = ".\database\database.db"

cg = CoinGeckoAPI()
#-------- NLU/NLP Channel list --------#
def load_cache_channel():
    # on_ready
    dbCon = sqlite3.connect(db_url)
    cur = dbCon.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS guilds (
        guild_id BIGINT PRIMARY KEY,
        nlu_channel_id BIGINT
    )""")
    cached_nlu_channels = [each[0] for each in cur.execute("""SELECT nlu_channel_id FROM guilds""").fetchall()]
    
    dbCon.commit()
    dbCon.close()
    return cached_nlu_channels

def add_nlu_channel(guild_id:int,nlu_channel_id:int):
    dbCon = sqlite3.connect(db_url)
    cur = dbCon.cursor()
    try:
        cur.execute(f"""INSERT INTO guilds values ({guild_id},{nlu_channel_id})""")
    except sqlite3.IntegrityError:
        cur.execute(f"""DELETE FROM guilds WHERE guild_id={guild_id}""")
        cur.execute(f"""INSERT INTO guilds values ({guild_id},{nlu_channel_id})""")
        # print("lol")
    dbCon.commit()
    dbCon.close()


# -------- On_StartUp -------- #
def write_coin_list():
    dbCon = sqlite3.connect(db_url)
    cur = dbCon.cursor()
    
    cl = cg.get_coins_list()
    cur.execute("""CREATE TABLE IF NOT EXISTS coin_list (id TEXT PRIMARY KEY,symbol TEXT NOT NULL, name TEXT NOT NULL)""")
    if cur.execute("SELECT COUNT(*) FROM coin_list").fetchall()[0][0] == len(cl):
        log.alert("Ignoring coin list Updation.")
    else:
        cur.execute("DELETE FROM coin_list")
        for each in cl:
            cur.execute(f'INSERT INTO coin_list VALUES ("{each["id"]}","{each["symbol"]}","{each["name"]}")')

        log.success("Coin list successfully refreshed! New supported amount of coins: " + str(len(cl)))
    
    dbCon.commit()
    dbCon.close()

def write_supported_currencies():
    dbCon = sqlite3.connect(db_url)
    cur = dbCon.cursor()
    
    gsc = cg.get_supported_vs_currencies()
    cur.execute("""CREATE TABLE IF NOT EXISTS supported_currencies (id TEXT)""")
    
    if cur.execute("SELECT COUNT(*) FROM supported_currencies").fetchall()[0][0] == len(gsc):
        log.alert("Ignoring supported currency Updation.")
    else:
        cur.execute("DELETE FROM supported_currencies")
        for each in gsc:
            cur.execute('INSERT INTO supported_currencies VALUES ("{0}")'.format(each))

        log.success("Supported Currency list successfully refreshed!")

    dbCon.commit()
    dbCon.close()

# -------- Basic Info -------- #
def get_top_company_holdings(coin_id:str):
    data = cg.get_companies_public_treasury_by_coin_id(coin_id=coin_id)
    data = data['companies']
    if len(data) > 10:
        count = 10
    else:
        count = len(data)
 
    embed = discord.Embed(title=f"Top {count} " + coin_id.capitalize() + " holding companies.",color=discord.Color.gold())
    for i in range(count):
        each = data[i]
        embed.add_field(
            name=f"{i+1} | " + each["name"] + " | :flag_{0}:".format(each["country"].lower().replace("japan","jp")),
            value=
f"""```yml
⩺ Total Holding: {each["total_holdings"]} 
⩺ Entry Value: {each["total_entry_value_usd"]} 
⩺ Current Value: {each["total_current_value_usd"]} 
⩺ % of Total Supply: {each["percentage_of_total_supply"]}
```""",inline=False
)
        embed.set_footer(text="Powered by CoinGecko",icon_url="https://imgur.com/67aeDXf.png")
    return embed
    
