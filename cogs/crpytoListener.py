from aiohttp import request
import discord
from discord.ext import commands
from discord.commands import slash_command,message_command,user_command
import utils.CryptoUtils as cu
import utils.databaseUtils as dbu
from requests.exceptions import HTTPError

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
        if message.author.bot or message.channel.id not in dbu.get_nlu_channels():
            return
        # TODO:- main
        await message.channel.send("Requesting NLU server...")
        

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
            raise error

def setup(bot):
    bot.add_cog(cryproListener(bot))