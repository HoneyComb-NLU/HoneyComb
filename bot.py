from datetime import datetime
from platform import platform
import discord 
from discord import file
import utils.osUtils as osu
import utils.consoleLogger as log
from decouple import config
from discord.ext import commands
import utils.databaseUtils as dbu

dgid = osu.get_debug_guilds()

bot = discord.Bot(
    activity=discord.Activity(
        type=discord.ActivityType.streaming,
        name="Soon!",url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ),
    status=discord.Status.idle,
    debug_guilds=dgid,
    owner_id=474589812192575488
)

def loadAllCogs():
    dir = osu.get_all_cogs()
    for each in dir:
        try:
            bot.load_extension(f"cogs.{each}")
        except discord.ExtensionError as dce:
            log.error(each.capitalize() + " cog loading Failed!")
            print(str(dce))
        else:
            log.success(each.capitalize() + " cog loaded Successfully!")

@bot.event
async def on_ready():
    log.info(f"Logged on as : {bot.user.name}")
    log.info(f"Debug Guilds : {dgid}")

@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(
        title="**Hey!! It's me, HoneyComb**.",
        timestamp=datetime.now(),
        description="""~~---------------------------------------------------------------------------------------------~~
First of all, __Thanks for adding me!__
I'm built to be your one stop solution for all your Crypto-currency related queries 
& I will try my level best to understand your Queries.
~~---------------------------------------------------------------------------------------------~~
**There are some things you should keep in mind while interacting with me.**
`⁕` I work in 2 modes, `Slash Command mode` & `Natural language mode`.
`⁕` Use `/setup` to set `Natural Language` query channel & default Exchange currencies.
`⁕` Natural language mode requires a special channel which should have atleast 30 seconds of [slow mode](https://support.discord.com/hc/en-us/articles/360016150952-Slowmode-Slllooowwwiiinng-down-your-channel).
`⁕` In order to use natural language mode use `/setchannel <channel>`.
`⁕` Natural language mode operates in **English only**. 
~~---------------------------------------------------------------------------------------------~~
Feel free to use `/help` if you get stuck.
""",
        color=discord.Color.gold()
    ).set_footer(text="By Team Hive Minds",icon_url=bot.user.avatar.url)
    log.info("[⇉] New Guild : " + guild.name)
    await guild.system_channel.send(embed=embed)

@bot.event
async def on_guild_remove(guild):
    dbu.remove_guild(guild.id)
    log.info("[⇇] Guild Leaved : " + guild.name)

# @bot.command()
# async def chart(ctx):
#     em = discord.Embed(title="Tether",description="Tether is a very popular Crypto-Currency!",color=discord.Color.gold())
#     file = discord.File("./assets/prices.png",filename="lolPrices.png")
#     em.set_image(url="attachment://lolPrices.png")
#     await ctx.respond(file=file,embed=em)



loadAllCogs()
# discord.http.API_VERSION = 10
bot.run(config("BOT_TOKEN"))



# @bot.command(name="load", description="Loads Cogs",guild_ids=dgid)
# async def load(ctx, cog: Option(str, "Enter Cog Name", choices=osu.get_all_cogs(), default="all", required=False)):
#     if cog == "all":        
#         loadAllCogs()
#     else:
#         try:
#             bot.load_extension(f"cogs.{cog}")
#         except discord.ExtensionAlreadyLoaded:
#             log.alert("Extension is alreay Loaded.")
#         except discord.ExtensionError:
#             log.error("Extension Error occured while loading " + cog)
#         else:
#             log.success(cog + " cog loaded Successfully!")


## Event

# @bot.event
# async def on_voice_state_update(member, before, after):
#     if before.channel is None and after.channel is not None:
#         await member.guild.system_channel.send(f"{member.mention} joined {after.channel.mention}")


# @bot.slash_command(name="hi",guild_ids=dgid)
# async def hello(ctx):
#     """Says Hello to you lol"""
#     await ctx.respond(f"Hello {ctx.author.mention}!",delete_after=5)
#     await ctx.invoke(bot.get_command(name="cmdwala"))

## Slash Command

# @bot.slash_command(name="test",guild_ids=dgid)
# async def test(ctx):
#     await ctx.respond("testing")
#     await bot.get_channel(920871875230441502).send("is this working?")

## Message Command

# @bot.message_command(name="Repeat",guild_ids=dgid)
# async def messageRepeat(ctx,message: discord.Message):
#     await ctx.respond(f'{message.content}')

## User Command

# @bot.user_command(name="Greet",guild_ids=dgid)
# async def userlol(ctx, user: discord.User):
#     await ctx.respond("Hello! "+user.mention)


## Embed + Embeded Image

# @bot.command(guild_ids=dgid)
# async def chart(ctx):
#     em = discord.Embed(title="Hmmm Embed",description="hmmmmmm",color=discord.Color.blurple())
#     file = discord.File("./assets/prices.png",filename="lolPrices.png")
#     em.set_image(url="attachment://lolPrices.png")
#     await ctx.respond(file=file,embed=em)
#     # await ctx.send(file=discord.File("./assets/prices.png"))

