import discord
from discord.ext import commands
from discord.commands import slash_command,message_command,user_command

class cryproListener(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self,ctx,error):
        if isinstance(error,commands.CommandOnCooldown):
            # if ctx.author.id in self.bot.owner_ids:
            #     await ctx.reinvoke()
            #     await ctx.send("sorry Boss!")
            embed = discord.Embed(
                title="Command Cooldown!",
                description=error,
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed,delete_after=5)
        else:
            raise error

def setup(bot):
    bot.add_cog(cryproListener(bot))