import asyncio
import discord
from discord.ext import commands
from discord.commands import slash_command,message_command,user_command
import utils.CryptoUtils as cu
import utils.databaseUtils as dbu
from requests.exceptions import HTTPError
import utils.consoleLogger as log

class cryproListener(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # force_reload_nlu()
        cached_nlu_channels = dbu.get_nlu_channels()
        print("Current Cached: " + str(cached_nlu_channels))
        cu.write_coin_list()
        cu.write_supported_currencies()

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot or message.channel.type == discord.ChannelType.private or not dbu.check_nlu_channels(message.channel.id):
            return

        delay_check_fail = message.channel.slowmode_delay < 30
        if delay_check_fail:
            em = discord.Embed(title="Slowmode not detected!",description="""In order to use Natural language mode you will need to have a minimum of 30 seconds slow mode...\n\n*Silently enables slowmode... hehehehe...*""",color=discord.Color.red())
            await message.channel.send(embed=em)
            await message.channel.edit(slowmode_delay=30)
            return
        
        
        # async with message.channel.typing():
        # # simulate something heavy
        #     # TODO:- main
        #     await asyncio.sleep(3)

        await message.channel.send(dbu.coin_id_check(message.content))
        # Smooth Love Potion -> smooth-love-potion

    @commands.Cog.listener()
    async def on_application_command_error(self,ctx,error):
        if isinstance(error,commands.CommandOnCooldown):            
            embed = discord.Embed(
                title="Command Cooldown!",
                description=error,
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed,delete_after=5)
        elif isinstance(error,HTTPError) and str(error)[:3] == "429":
            embed = discord.Embed(
                title="**Wow! Nice Burnout!**",
                description=f"Data request limit exceeded! Please ask the <@474589812192575488> to pay for the services. ",
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed)

        else:
            log.error(str(error))
            # raise error

def setup(bot):
    bot.add_cog(cryproListener(bot))