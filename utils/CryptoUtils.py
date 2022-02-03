from pycoingecko import CoinGeckoAPI
import discord 
import utils.consoleLogger as log

cg = CoinGeckoAPI()
# -------- On_StartUp -------- #
def write_coin_list():
    with open("./database/coin_list.json", 'w') as cl:
        cl.write(cg.get_coins_list())
    log.success("Coin List successfully refreshed!")

def write_coin_catergory_list():
    with open("./database/coin_category_list.json", 'w') as ccl:
        ccl.write(cg.get_coins_categories_list())
    log.success("Coin Category list successfully refreshed!")

def write_supported_currencies():
    with open("./database/supported_currencies.json", 'w') as sc:
        sc.write(cg.get_supported_vs_currencies())
    log.success("Supported Currency list successfully refreshed!")

def write_indexes_list():
    with open("./database/index_list.json", 'w') as il:
        il.write(cg.get_indexes_list())
    log.success("Index List successfully refreshed!")

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
    return embed
    
