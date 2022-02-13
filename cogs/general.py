import discord
import utils.osUtils as osu
from discord.commands import slash_command,message_command,user_command
from discord.commands import Option
from discord.ext import commands
import random

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

def setup(bot):
    bot.add_cog(General(bot))