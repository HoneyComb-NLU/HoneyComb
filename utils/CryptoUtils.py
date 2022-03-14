from datetime import datetime
from pycoingecko import CoinGeckoAPI
import sqlite3,json,re
import discord
from discord.ext import pages
import utils.consoleLogger as log
import utils.osUtils as osu
import utils.databaseUtils as dbu
from tabulate import tabulate as tb
import utils.chartUtils as chrt

db_url = osu.get_db()
# db_url = ".\database\database.db"
# embed.set_footer(text="Powered by CoinGecko",icon_url="https://imgur.com/67aeDXf.png")

cg = CoinGeckoAPI()

# ----------- Aux ------------- #
def multiple_currency_extractor(List:list,data,signed:bool=False):
    """Extract the given currencies. Returns list of tuples of key values"""
    lol = []
    for e in List:
        lol.append([e.upper(),str(round(data[e],8))])
    if signed:
        for e in lol:
            e[1] += "↑" if float(e[1]) > 0 else "↓"
    return lol

def get_Paginator_buttons():
    return [
        pages.PaginatorButton(
            button_type="first",emoji=discord.PartialEmoji.from_str("HCrewind:943916100435992668"),style=discord.ButtonStyle.gray
        ),
        pages.PaginatorButton(
            button_type="prev",emoji=discord.PartialEmoji.from_str("HCprevious:943916099496460328"),style=discord.ButtonStyle.gray
        ),
        pages.PaginatorButton(
            "page_indicator", style=discord.ButtonStyle.gray, disabled=True
        ),
        pages.PaginatorButton(
            button_type="next",emoji=discord.PartialEmoji.from_str("HCnext:943916099341254686"),style=discord.ButtonStyle.gray
        ),
        pages.PaginatorButton(
            button_type="last",emoji=discord.PartialEmoji.from_str("HCfastfwd:943916100880564304"),style=discord.ButtonStyle.gray
        )
    ]

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

def get_price(guild_id:int,id:str,vs_currency:str=None,mkt_cap=False):
    if vs_currency == None:
        vs_currency = dbu.get_default_currency(guild_id)

    id = id.replace(", ",",").replace(" ","-").lower()
    
    vs_currency = str(vs_currency).replace(" ","").lower()
    id_list = id.split(",")
    vs_currency_list = vs_currency.split(",")

    # ---- Database Validation ---- #
    for i in range(len(id_list)):
        id_list[i] = dbu.coin_id_check(id_list[i])
        assert id_list[i] != '',"Coin Id Mismatch : " + id_list[i]
        
    for e in vs_currency_list:
        assert len(dbu.supported_currency_check(e)) != 0,"Vs Currency Mismatch" + e

    id = ','.join(id_list)
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

def page_coin_details(guild_id:int,id:str,vs_currency:str):
    # ---------- Pre-processing ----------#
    if vs_currency == None:
        vs_currency = dbu.get_default_currency(guild_id)

    id = dbu.coin_id_check(id.replace(" ","-").lower())
    vs_currency = str(vs_currency).replace(" ","").lower()
    
    vs_currency_list = vs_currency.split(",")
    # TODO: give multiple currency support?
    # ---- Database Validation ---- #

    assert len(id) != 0,"Coin Id Mismatch : " + id
    for e in vs_currency_list:
        assert len(dbu.supported_currency_check(e)) != 0,"Vs Currency Mismatch : " + e

    # ------- Main Stuff ------#
    data = cg.get_coin_by_id(id=id,localization="false",tickers=False,market_data=True,community_data=False,developer_data=False,sparkline=False)
    # ---- 1
    data_pages = [
        discord.Embed(
            title="**__" + data["name"] + "__ ┋ __" + str(data["symbol"]).upper() + "__**",
            description=re.sub("<a.*?>","",str(data["description"]["en"][:1024])).replace("</a>","").replace("\n\n\n","\n\n") + "...",
            url=f"https://www.coingecko.com/en/coins/{id}",
            color=discord.Color.gold(),
            timestamp=datetime.now()
        )
        .set_author(name="Description")
        .set_thumbnail(url=data['image']['large'])
        .set_footer(text="Powered by CoinGecko",icon_url="https://imgur.com/67aeDXf.png")
    ]
    # ---- 2
    data_pages.append(
        discord.Embed(
            title="**__" + data["name"] + "__ ┋ __" + str(data["symbol"]).upper() + "__**",
            url=f"https://www.coingecko.com/en/coins/{id}",
            color=discord.Color.gold(),
            timestamp=datetime.now() 
        )
        .set_author(name="Price")
        .set_thumbnail(url=data['image']['large'])
        .set_footer(text="Powered by CoinGecko",icon_url="https://imgur.com/67aeDXf.png")
        .add_field(
            name="**Current __Price__ :**",
            value="```ml\n" + tb(
                multiple_currency_extractor(vs_currency_list,data['market_data']['current_price']),
                tablefmt='fancy_grid',
                numalign="left"
            ) + "```",
            inline=True
        )
        .add_field(
            name="**__Price__ Change in 24Hrs :**",
            value="```ml\n" + tb(
                multiple_currency_extractor(vs_currency_list,data['market_data']['price_change_24h_in_currency'],True),
                tablefmt='fancy_grid',
                numalign="left"
            ) + "```",
            inline=True
        )
        .add_field(
            name="**__Price__ change % [1D] :**",
            value= ":small_orange_diamond: " + str(round(data['market_data']['price_change_percentage_24h'],2)),
            inline=False
        )
        # .add_field(
        #     name="**__Price__ change % [1M] :**",
        #     value= "**:small_orange_diamond: " + str(round(data['market_data']['price_change_percentage_30d'],2)) + "% **",
        #     inline=True
        # )
        .add_field(
            name="**All Time __High__ :**",
            value="```ml\n" + tb(
                multiple_currency_extractor(vs_currency_list,data['market_data']['ath']),
                tablefmt='fancy_grid',
                numalign="left"
            ) + "```",
            inline=True
        )
        .add_field(
            name="**All Time __Low__ :**",
            value="```ml\n" + tb(
                multiple_currency_extractor(vs_currency_list,data['market_data']['atl']),
                tablefmt='fancy_grid',
                numalign="left"
            ) + "```",
            inline=True
        )
        
        # .add_field(
        #     name="**__Price__ change % [1Y] :**",
        #     value= "**:small_orange_diamond: " + str(round(data['market_data']['price_change_percentage_1y'],4)) + "**",
        #     inline=True
        # )
        
    )
    # ---- 3
    data_pages.append(
        discord.Embed(
            title="**__" + data["name"] + "__ ┋ __" + str(data["symbol"]).upper() + "__**",
            url=f"https://www.coingecko.com/en/coins/{id}",
            color=discord.Color.gold(),
            timestamp=datetime.now() 
        )
        .set_author(name="Market Capitalization & Supply")
        .set_thumbnail(url=data['image']['large'])
        .set_footer(text="Powered by CoinGecko",icon_url="https://imgur.com/67aeDXf.png")
        .add_field(
            name="**__Market Cap__ Rank :**",
            value= ":small_orange_diamond: " + str(data['market_cap_rank']),
            inline=False
        )
        .add_field(
            name="**__Market Cap__ Change % [1D] :**",
            value= ":small_orange_diamond: " + str(data['market_data']['market_cap_change_percentage_24h']),
            inline=False
        )
        .add_field(
            name="**Total __Supply__ :**",
            value= ":small_orange_diamond: " + str(data['market_data']['total_supply']),
            inline=False
        )
        .add_field(
            name="**Circulating __Supply__ :**",
            value= ":small_orange_diamond: " + str(data['market_data']['circulating_supply']),
            inline=False
        )
        .add_field(
            name="**Total __Volume__ :**",
            value="```ml\n" + tb(
                multiple_currency_extractor(vs_currency_list,data['market_data']['total_volume']),
                tablefmt='fancy_grid',
                numalign="left"
            ) + "```",
            inline=False
        )
    )

    # print(data_pages)
    return data_pages

def make_normal_chart(coin_id:str, vs_curr:str, days:str, type:str, user_id:str, guild_id:int):
    coin_id = dbu.coin_id_check(coin_id.replace(" ","-").lower())
    assert len(coin_id) != 0

    embed = discord.Embed(
        title=f"{dbu.get_coin_name(coin_id).capitalize()}'s {type} for last `{days}` days",
        color=discord.Color.gold(),
        timestamp=datetime.now()
    )
    
    # print(">" + coin_id)
    if vs_curr == None:
        vs_curr = dbu.get_default_currency(guild_id=guild_id)
        vs_curr = str(vs_curr).replace(" ","").lower().split(",")[0]


    image_name = f"{user_id}_{datetime.now().timestamp()}"
    chrt.make_chart(coin_id,vs_curr,days,type[:1].lower(),image_name)

    img = discord.File(f"./charts/{image_name}.png",filename=f"chart.png")
    embed.set_image(url=f"attachment://chart.png")

    return embed,img,image_name

def make_ohlc_chart(coin_id:str, vs_curr:str, days:str, user_id:str, guild_id:int):
    coin_id = dbu.coin_id_check(coin_id.replace(" ","-").lower())
    assert len(coin_id) != 0

    embed = discord.Embed(
        title=f"{dbu.get_coin_name(coin_id).capitalize()}'s OHLC Price for last `{days}` days",
        color=discord.Color.gold(),
        timestamp=datetime.now()
    )
    
    # print(">" + coin_id)
    if vs_curr == None:
        vs_curr = dbu.get_default_currency(guild_id=guild_id)
        vs_curr = str(vs_curr).replace(" ","").lower().split(",")[0]


    image_name = f"{user_id}_{datetime.now().timestamp()}"
    chrt.make_ohlc_chart(coin_id,vs_curr,days,image_name)

    img = discord.File(f"./charts/{image_name}.png",filename=f"chart.png")
    embed.set_image(url=f"attachment://chart.png")

    return embed,img,image_name

def make_ranged_chart(coin_id:str, vs_curr:str, from_timedelta:int, to_timedelta:int, type:str, user_id:str, guild_id:int):
    coin_id = dbu.coin_id_check(coin_id.replace(" ","-").lower())
    assert len(coin_id) != 0

    if vs_curr == None:
        vs_curr = dbu.get_default_currency(guild_id=guild_id)
        vs_curr = str(vs_curr).replace(" ","").lower().split(",")[0]


    embed = discord.Embed(
        title=f"{dbu.get_coin_name(coin_id).capitalize()}'s {type} from `{datetime.strftime(datetime.fromtimestamp(from_timedelta),'%d %b, %Y')}` to `{datetime.strftime(datetime.fromtimestamp(to_timedelta),'%d %b, %Y')}`",
        color=discord.Color.gold(),
        timestamp=datetime.now()
    )

    
    image_name = f"{user_id}_{datetime.now().timestamp()}"
    chrt.make_ranged_chart(coin_id,vs_curr,from_timedelta,to_timedelta,type[:1].lower(),image_name)

    img = discord.File(f"./charts/{image_name}.png",filename=f"chart.png")
    embed.set_image(url=f"attachment://chart.png")

    return embed,img,image_name


