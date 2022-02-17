from calendar import c
import discord
from discord.ext import commands
from discord.commands import slash_command,message_command,user_command,CommandPermission,SlashCommandGroup
from discord.commands import permissions
import utils.consoleLogger as log
import discord.ext.commands.cooldowns as cd
import utils.CryptoUtils as cu


class Owner_Commands(commands.Cog,name="Owner Commands"):
    def __init__(self,bot):
        self.bot = bot

    @slash_command(default_permission=False)
    @permissions.is_owner()
    async def exit(self,ctx):
        await ctx.respond("Exiting!",ephemeral=True)
        log.alert(f"Exit Command executed by: {ctx.author.name}#{ctx.author.discriminator}")
        await self.bot.close()
    
    # @slash_command(default_permission=False,description="Refresh all the Startup Lists Manually.")
    # @permissions.is_owner()
    # @commands.cooldown(1,10,commands.BucketType.user)
    # async def refresh(self,ctx):        
        
    #     await ctx.respond(embed=discord.Embed(title=""))
    #     log.alert(f"Refresh Command executed by: {ctx.author.name}#{ctx.author.discriminator}")


def setup(bot):
    bot.add_cog(Owner_Commands(bot))