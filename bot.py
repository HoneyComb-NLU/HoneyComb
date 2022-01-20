from datetime import datetime
import discord as dc
from discord import file
from discord.embeds import Embed
import utils.osUtils as osu
import utils.consoleLogger as log
from decouple import config

# from discord import discord

dgid = osu.get_debug_guilds()

bot = dc.Bot(
    activity=dc.Activity(type=dc.ActivityType.listening,name="Slash Commands ;-;"),
    status=dc.Status.dnd,
    debug_guilds=dgid,
    owner_id=474589812192575488
)

def loadAllCogs():
    dir = osu.get_all_cogs()
    for each in dir:
        try:
            bot.load_extension(f"cogs.{each}")
        except dc.ExtensionError as dce:
            log.error(each.capitalize() + " cog loading Failed!")
            print(str(dce))
        else:
            log.success(each.capitalize() + " cog loaded Successfully!")

@bot.event
async def on_ready():
    log.info(f"Logged on as : {bot.user.name}")
    log.alert(f"Slash commands active on : {dgid}")
 

@bot.command()
async def chart(ctx):
    em = dc.Embed(title="Tether",description="Tether is a very popular Crypto-Currency!",color=dc.Color.gold())
    file = dc.File("./assets/prices.png",filename="lolPrices.png")
    em.set_image(url="attachment://lolPrices.png")
    await ctx.respond(file=file,embed=em)


# @bot.command()
# async def owner(ctx):
#     await ctx.respond(bot.owner_ids.set())

loadAllCogs()

bot.run(config("BOT_TOKEN"))



# @bot.command(name="load", description="Loads Cogs",guild_ids=dgid)
# async def load(ctx, cog: Option(str, "Enter Cog Name", choices=osu.get_all_cogs(), default="all", required=False)):
#     if cog == "all":        
#         loadAllCogs()
#     else:
#         try:
#             bot.load_extension(f"cogs.{cog}")
#         except dc.ExtensionAlreadyLoaded:
#             log.alert("Extension is alreay Loaded.")
#         except dc.ExtensionError:
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
# async def messageRepeat(ctx,message: dc.Message):
#     await ctx.respond(f'{message.content}')

## User Command

# @bot.user_command(name="Greet",guild_ids=dgid)
# async def userlol(ctx, user: dc.User):
#     await ctx.respond("Hello! "+user.mention)


## Embed + Embeded Image

# @bot.command(guild_ids=dgid)
# async def chart(ctx):
#     em = dc.Embed(title="Hmmm Embed",description="hmmmmmm",color=dc.Color.blurple())
#     file = dc.File("./assets/prices.png",filename="lolPrices.png")
#     em.set_image(url="attachment://lolPrices.png")
#     await ctx.respond(file=file,embed=em)
#     # await ctx.send(file=dc.File("./assets/prices.png"))

