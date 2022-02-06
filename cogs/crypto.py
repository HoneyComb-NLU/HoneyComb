from random import choices
import utils.CryptoUtils as cu
import discord
import cogs.crpytoListener as cc
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

    @slash_command(description="Get public companies bitcoin or ethereum holdings.")
    @commands.cooldown(1,10,commands.BucketType.user)
    async def setchannel(self, ctx, channel: Option(discord.TextChannel,description="Channel where Bot should listen for Natural Language",required=True)):
        cu.add_nlu_channel(ctx.guild.id,channel.id)
        # cc.force_reload_nlu()
        embed = discord.Embed(title="Natural Language Mode",description=f"HoneyComb is now listening for Natural language in <#{channel.id}>",color=discord.Color.brand_green())
        await ctx.respond(embed=embed,delete_after=15)
        newChannelEmbed = discord.Embed(title="Natural Language Mode",description=f"HoneyComb is now listening for Natural language in this channel!",color=discord.Color.brand_green())
        await channel.send(embed=newChannelEmbed)    

    @slash_command(description="Da Tester!")
    async def da_baby(self,ctx):
        pass
        


    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print("In the COG POG!!")

    


def setup(bot):
    bot.add_cog(Crypto(bot))