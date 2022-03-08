from locale import currency
import discord
import utils.osUtils as osu
from discord.commands import slash_command,message_command,user_command
from discord.commands import Option
from discord.ext import commands,pages
import utils.databaseUtils as dbu

dgid = osu.get_debug_guilds()

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(description="Check bot's Latency.")
    async def ping(self,ctx):
        pingembed = discord.Embed(
            title=f"""{str(int(self.bot.latency * 1000)) + " ms"}""",
            color=discord.Color.embed_background()
        )
        await ctx.respond(embed=pingembed)

    @slash_command(description="Get Guild specific data.")
    async def info(self,ctx:discord.ApplicationContext):
        def_curr = dbu.get_default_currency(ctx.guild_id)
        nlu_chnl = dbu.get_guild_nlu_channel(ctx.guild_id)

        await ctx.respond(
            embed=discord.Embed(
                title=f"{ctx.guild.name}'s Info",
                description=f":small_orange_diamond: I am listening to queries in English in <#{nlu_chnl}>.\n:small_orange_diamond: Default Currency(s) of this Guild are: `{def_curr.upper().replace(',',', ')}`",
                color=discord.Color.embed_background()
            )
        )



def setup(bot):
    bot.add_cog(General(bot))