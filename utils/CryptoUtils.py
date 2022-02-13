from datetime import datetime
from pycoingecko import CoinGeckoAPI
import sqlite3
import discord
import utils.consoleLogger as log
import utils.osUtils as osu
import utils.databaseUtils as dbu
from tabulate import tabulate as tb


db_url = osu.get_db()
# db_url = ".\database\database.db"
# embed.set_footer(text="Powered by CoinGecko",icon_url="https://imgur.com/67aeDXf.png")

cg = CoinGeckoAPI()

#-------- NLU/NLP Channel list --------#
def load_cache_channel():
    # on_ready
    dbCon = sqlite3.connect(db_url)
    cur = dbCon.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS guilds (
        guild_id BIGINT PRIMARY KEY,
        nlu_channel_id BIGINT,
        default_vs_currency TEXT DEFAULT 'INR'
    )""")
    cached_nlu_channels = [each[0] for each in cur.execute("""SELECT nlu_channel_id FROM guilds""").fetchall()]
    
    dbCon.commit()
    dbCon.close()
    return cached_nlu_channels

def add_nlu_channel(guild_id:int,nlu_channel_id:int,default_vs_currency:str):
    dbCon = sqlite3.connect(db_url)
    cur = dbCon.cursor()

    default_vs_currency = str(default_vs_currency).replace(" ","").lower()
    vs_currency_list = default_vs_currency.split(",")

    for e in vs_currency_list:
        if len(dbu.supported_currency_check(e)) == 0:
            return False

    try:
        cur.execute(f"""INSERT INTO guilds values ({guild_id},{nlu_channel_id},"{default_vs_currency}")""")
    except sqlite3.IntegrityError:
        cur.execute(f"""DELETE FROM guilds WHERE guild_id={guild_id}""")
        cur.execute(f"""INSERT INTO guilds values ({guild_id},{nlu_channel_id},"{default_vs_currency}")""")
        # print("lol")
    dbCon.commit()
    dbCon.close()
    return True


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

# -------- Main Stuff -------- #
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
        val_list = [
            ["Total Holding", each["total_holdings"]],
            ["Entry Value", each["total_entry_value_usd"]],
            ["Current Value", each["total_current_value_usd"]],
            ["% Of Total Supply", each["percentage_of_total_supply"]]
        ]
        embed.add_field(
            name=f"{i+1} | " + each["name"] + " | :flag_{0}:".format(each["country"].lower().replace("japan","jp")),
            value=f"""```ml\n{tb(val_list,tablefmt="fancy_grid",numalign="center",floatfmt=(".3f"))}```""",inline=False)
        embed.set_footer(text="Powered by CoinGecko",icon_url="https://imgur.com/67aeDXf.png")
    return embed
    
def get_supported_currencies():
    data = dbu.get_all_currencies()
    nl = []
    for i in range(len(data)):
        if i % 7 == 0:
            nl.append([])
        nl[-1].append(data[i].upper())
    # print(nl)
    emb = discord.Embed(
        title="Supported Currencies",
        description=f"```\n{tb(nl,tablefmt='fancy_grid')}```"
    )
    return emb

def get_price(id:str,guild_id,vs_currency:str=None,mkt_cap=False):
    if vs_currency == None:
        vs_currency = dbu.get_default_currency(guild_id)

    id = id.replace(", ",",").replace(" ","-").lower()
    vs_currency = str(vs_currency).replace(" ","").lower()
    id_list = id.split(",")
    vs_currency_list = vs_currency.split(",")

    # ---- Database Validation ---- #
    for e in id_list:
        if len(dbu.coin_id_check(e)) == 0:
            raise KeyError("Coin Id Mismatch : " + e)
        
    for e in vs_currency_list:
        if len(dbu.supported_currency_check(e)) == 0:
            raise KeyError("Vs Currency Mismatch : " + e)

    # ----- Limit ------- #
    if id.count(',') >= 5 or vs_currency.count(",") >= 5:
        err = discord.Embed(title="Woaahh! Why are you so Data-Hungry...",description="You can only request up to **5** ids & **5** Exchange currencies at a time.",
        color=discord.Color.red(),timestamp=datetime.now())
        return err

    data = cg.get_price(ids=id,vs_currencies=vs_currency,include_market_cap=mkt_cap)
    
    embed = discord.Embed(title="Here are the price(s) you asked!",color=discord.Color.gold(),timestamp=datetime.now())
    for i in id_list:
        tempLs = []
        for j in vs_currency_list:
            tempLs.append([
                f"{j.upper()} | Price", data[i][j]
            ])

            if mkt_cap:
                tempLs.append([
                    f"{j.upper()} | Market Cap.", data[i][f"{j}_market_cap"]
                ])
        embed.add_field(
            name=f"**{i.capitalize().replace('-',' ')}**",
            value=f"""```ml\n{tb(tempLs,tablefmt="fancy_grid",numalign="center")}```""",
            inline=False)
    embed.set_footer(text="Powered by CoinGecko",icon_url="https://imgur.com/67aeDXf.png")
    return embed

def searching(query):
    data = dbu.search_thru_db_for(query)

    if len(data) > 0:
        head = ["Id", "Symbol", "Name"]
        em = discord.Embed(
            title="Search results for " + f"`{query}`",
            description="```\n" + tb(data,headers=head,numalign="center",stralign="left",tablefmt="fancy_grid") + "```",
            timestamp=datetime.now(),
            color=discord.Color.gold()
        )
    else:
        em = discord.Embed(
            title=f"No result found for `{query}` :(",
            timestamp=datetime.now(),
            color=discord.Color.red()
        )

    return em

