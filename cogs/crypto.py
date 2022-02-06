from random import choices
import utils.CryptoUtils as cu
import discord
from discord.commands import slash_command,Option
from discord.ext import commands
# Chart_url = "https://quickcharts.io/charts?c="


class Crypto(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @slash_command(description="Get public companies bitcoin or ethereum holdings.")
    @commands.cooldown(1,30,commands.BucketType.user)
    async def global_holdings(self, ctx, coin_id: Option(str,description="Coin Id",choices=["Bitcoin","Ethereum"],required=True)):
        await ctx.respond(embed=cu.get_top_company_holdings(coin_id.lower()))

    @slash_command(description="Da Tester!")
    async def da_baby(self,ctx):
        # cu.load_cache_channel()
        c = cu.temp()
        
        await ctx.respond(c.cached_nlu_channels)
        await ctx.send(cu.cached_nlu_channels)
        


    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print("In the COG POG!!")

    


def setup(bot):
    bot.add_cog(Crypto(bot))