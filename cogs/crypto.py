import utils.osUtils as osu
from discord.commands import slash_command
import requests
from discord.ext import commands
# Chart_url = "https://quickcharts.io/charts?c="

dgid = osu.get_debug_guilds()

class Crypto(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @slash_command(guild_ids=dgid)
    async def cryptolol(self,ctx):
        await ctx.respond("Hi, Crypto is a Very Volatile market :|")


    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print("In the COG POG!!")

    


def setup(bot):
    bot.add_cog(Crypto(bot))