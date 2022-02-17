import discord
import utils.osUtils as osu
from discord.commands import slash_command,message_command,user_command
from discord.commands import Option
from discord.ext import commands,pages
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

    @slash_command(name="target")
    async def pagetest_target(self, ctx: discord.ApplicationContext):
        """Demonstrates sending the paginator to a different target than where it was invoked."""
        paginator = pages.Paginator(pages=["11111", "22222", "33333"])
        await paginator.respond(ctx.interaction, target=ctx.interaction.user)
    







def setup(bot):
    bot.add_cog(General(bot))