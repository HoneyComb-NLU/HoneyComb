from pydoc import describe
from random import choices
import utils.CryptoUtils as cu
import utils.databaseUtils as dbu
import discord
import cogs.crpytoListener as cc
from discord.commands import slash_command,Option
from discord.ext import commands
# Chart_url = "https://quickcharts.io/charts?c="

class Crypto(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    # --------------- Auxilary Commands ------------- #
    @slash_command(description="Get public companies bitcoin or ethereum holdings.")
    @commands.cooldown(1,10,commands.BucketType.user)
    async def setchannel(self, ctx, channel: Option(discord.TextChannel,description="Channel where Bot should listen for Natural Language",required=True)):
        cu.add_nlu_channel(ctx.guild.id,channel.id)
        await channel.edit(slowmode_delay=30,topic="<@920869009057017907>'s natural language queries channel.")
        embed = discord.Embed(title="Natural Language Mode",description=f"HoneyComb is now listening for Natural language in <#{channel.id}>",color=discord.Color.brand_green())
        await ctx.respond(embed=embed,delete_after=15)
        newChannelEmbed = discord.Embed(title="Natural Language Mode",description=f"HoneyComb is now listening for Natural language in this channel!",color=discord.Color.brand_green())
        await channel.send(embed=newChannelEmbed)    

    @slash_command(description="Da Tester!")
    async def da_baby(self,ctx):
        pass
    

    # ----------- Main Commands ------------- #
    @slash_command(description="Get public companies bitcoin or ethereum holdings.")
    @commands.cooldown(1,30,commands.BucketType.user)
    async def global_holdings(self, ctx, coin_id: Option(str,description="Coin Id",choices=["Bitcoin","Ethereum"],required=True)):
        await ctx.respond(embed=cu.get_top_company_holdings(coin_id.lower()))

    @slash_command(description="Get public companies bitcoin or ethereum holdings.")
    @commands.cooldown(1,30,commands.BucketType.user)
    async def supported_currencies(self,ctx):
        await ctx.respond(embed=cu.get_supported_currencies())

    @slash_command(description="Get the current price of any listed crytpocurrencies in any supported currencies.")
    @commands.cooldown(1,30,commands.BucketType.user)
    async def price(self,ctx,id: Option(str,description="Id of coins, comma-separated if querying more than 1 coin",required=True),
    currency: Option(str,description="Conversion currency, comma-separated if querying more than 1 currency. [/supported_currencies]",required=True),
    market_cap: Option(bool,description="Whether you want Market capitalization info of the coin(s)",required=False)):
        await ctx.respond(embed=cu.get_price(id,currency,market_cap))

    @price.error
    async def err(self,ctx,error):
        if isinstance(error,discord.ApplicationCommandInvokeError):
            await ctx.respond(embed=discord.Embed(
                title="Token Name Error",
                description="Please input **valid** crypto/exchange id.",
                color=discord.Color.red()
            ))

def setup(bot):
    bot.add_cog(Crypto(bot))