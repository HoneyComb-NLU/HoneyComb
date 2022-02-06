from aiohttp import request
import discord
from discord.ext import commands
from discord.commands import slash_command,message_command,user_command
import utils.CryptoUtils as cu
from requests.exceptions import HTTPError

ProductionStage = True
cst = []
class cryproListener(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        cst = cu.load_cache_channel()
        if ProductionStage:
            cu.write_coin_list()
            cu.write_supported_currencies()

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return
        await message.channel.send(cu.cached_nlu_channels)
        await message.channel.send(cst)
        pass

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
        elif isinstance(error,HTTPError) and str(error)[:3] == "429":
            embed = discord.Embed(
                title="**Wow! Nice Burnout!**",
                description=f"Data request limit exceeded! Please ask the <@474589812192575488> to pay for the services. ",
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed)

        else:
            raise error

def setup(bot):
    bot.add_cog(cryproListener(bot))