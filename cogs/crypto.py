from datetime import datetime
from email.policy import default
import utils.CryptoUtils as cu
import utils.databaseUtils as dbu
import discord
import cogs.crpytoListener as cc
from discord.commands import slash_command,Option,permissions
from discord.ext import commands,pages
from tabulate import tabulate as tb

# Chart_url = "https://quickcharts.io/charts?c="

class Crypto(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    # --------------- Auxilary Commands ------------- #
    
    @slash_command(description="Set the channel where Honeycomb should listen for natural language queries.")
    @commands.cooldown(1,10,commands.BucketType.user)
    @commands.has_guild_permissions(administrator=True)
    async def setup(self, ctx, nlu_channel: Option(discord.TextChannel,description="Channel where Bot should listen for Natural Language"),
    default_exhange_currency: Option(str,description='Eg. INR, USD, etc | Defaults to "INR" [/supported_currencies]',required=False,default="INR")):        
        if default_exhange_currency.count(",") >= 5:
            erremb = discord.Embed(title="Default Exchange currencies limit exceeded!",
            description="You can only have upto 5 default exchange currecies.",color=discord.Color.red())
            await ctx.respond(embed=erremb)
            return

        err = cu.add_nlu_channel(ctx.guild.id,nlu_channel.id,default_exhange_currency)

        if not err:
            await ctx.respond(embed=discord.Embed(title="There was some Error!",description="There was some error in your given data please double check the values.\n`⁕` Please refer to `/supported_currencies` to see out supported currencies.",
            color=discord.Color.red()))
            return

        await nlu_channel.edit(slowmode_delay=30,topic="<@920869009057017907>'s natural language queries channel.")
        embed = discord.Embed(title="Natural Language Mode",description=f"""HoneyComb is now listening for Natural language in <#{nlu_channel.id}>""",color=discord.Color.brand_green())
        await ctx.respond(embed=embed,delete_after=30)
        newChannelEmbed = discord.Embed(title="Natural Language Mode",description=f"HoneyComb is now listening for Natural language in this channel!\n**New Default Currency(ies) : ** {default_exhange_currency}",color=discord.Color.brand_green())
        await nlu_channel.send(embed=newChannelEmbed)
         

    #TODO: add removechannel command
    
    @slash_command(description="Helps you find Id, Symbol or Name of the Cryptocurrency.")
    @commands.cooldown(1,10,commands.BucketType.user)
    async def search(self,ctx,query: Option(str, description="Enter your Query string here, E.g. Matic, btc, ETH, etc",required=True)):
        await ctx.respond(embed=cu.searching(query))
        print(self.bot.get_user(474589812192575488))
        print(type(self.bot.get_user(474589812192575488)))


    # ----------- Main Commands ------------- #

    #TODO: make search in to crypto grp

    @slash_command(description="Helps you find Id, Symbol or Name of the Cryptocurrency.")
    @commands.cooldown(1,10,commands.BucketType.user)
    async def search(self,ctx,query: Option(str, description="Enter your Query string here, E.g. Matic, btc, ETH, etc",required=True)):
        await ctx.respond(embed=cu.searching(query))

    @slash_command(description="Get public companies bitcoin or ethereum holdings.")
    @commands.cooldown(1,30,commands.BucketType.user)
    async def global_holdings(self, ctx, coin_id: Option(str,description="Coin Id",choices=["Bitcoin","Ethereum"],required=True)):
        await ctx.respond(embed=cu.get_top_company_holdings(coin_id.lower()))

    @slash_command(description="Get a list of all the supported Exchange currencies.")
    @commands.cooldown(1,30,commands.BucketType.user)
    async def supported_currencies(self,ctx):
        await ctx.respond(embed=cu.get_supported_currencies())

    @slash_command(description="Get the current price of any listed crytpocurrencies in any supported currencies.")
    @commands.cooldown(1,30,commands.BucketType.user)
    async def price(self,ctx,id: Option(str,description="Id of coins, comma-separated if querying more than 1 coin",required=True),
    currency: Option(str,description="Conversion currency, comma-separated if querying more than 1 currency. [/supported_currencies]",required=False),
    market_cap: Option(bool,description="Whether you want Market capitalization info of the coin(s)",required=False)):
        await ctx.respond(embed=cu.get_price(ctx.guild.id,id,currency,market_cap))

    @price.error
    async def err(self,ctx,error):
        if isinstance(error,discord.ApplicationCommandInvokeError):
            await ctx.respond(embed=discord.Embed(
                title="Token Name Error",
                description="Please input **__Valid__** crypto/exchange id.",
                color=discord.Color.red()
            ),ephemeral=True)



    @slash_command(description="Get curcial data of the given coin.")
    @commands.cooldown(1,30,commands.BucketType.user)
    async def coin_data(self,ctx: discord.ApplicationContext, id: Option(str,description="Id of coin",required=True),
    currency: Option(str,description="Conversion currency, comma-separated if querying more than 1 currency. [/supported_currencies]",required=False)):
        
        resPaginator = pages.Paginator(pages=list(cu.page_coin_details(guild_id=ctx.guild.id,id=id,vs_currency=currency)),timeout=60)
        await resPaginator.respond(ctx.interaction, ephemeral=False)
        
def setup(bot):
    bot.add_cog(Crypto(bot))