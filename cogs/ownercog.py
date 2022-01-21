from email.policy import default
import discord
from discord.ext import commands
from discord.commands import slash_command,message_command,user_command,CommandPermission,SlashCommandGroup
from discord.commands import permissions
import utils.consoleLogger as log

class Owner_Commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @slash_command(default_permission=False)
    @permissions.is_owner()
    async def exit(self,ctx):
        await ctx.respond("Exiting!")
        log.alert(f"Exit Command executed by: {ctx.author.name}#{ctx.author.id}")
        await self.bot.close()
        

def setup(bot):
    bot.add_cog(Owner_Commands(bot))