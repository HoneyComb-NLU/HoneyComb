import asyncio
import discord
from discord.ext import commands
from discord.commands import slash_command,message_command,user_command
import utils.CryptoUtils as cu
import utils.databaseUtils as dbu
from requests.exceptions import HTTPError

class cryproListener(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # force_reload_nlu()
        cached_nlu_channels = dbu.get_nlu_channels()
        print("Current Cached: " + str(cached_nlu_channels))
        cu.write_coin_list()
        cu.write_supported_currencies()

    @commands.Cog.listener()
    async def on_message(self,message):
        delay_check = message.channel.slowmode_delay < 30
        if message.author.bot or message.channel.id not in dbu.get_nlu_channels() or delay_check:
            if delay_check:
                em = discord.Embed(title="Slowmode not detected!",description="""In order to use Natural language mode you will need to have a minimum of 30 seconds [slow mode](https://support.discord.com/hc/en-us/articles/360016150952-Slowmode-Slllooowwwiiinng-down-your-channel)""")
                await message.channel.send(embed=em)
            return
        

        async with message.channel.typing():
        # simulate something heavy
            # TODO:- main
            await asyncio.sleep(3)

        await message.channel.send("Requesting NLU server...")
        # Smooth Love Potion -> smooth-love-potion

    @commands.Cog.listener()
    async def on_application_command_error(self,ctx,error):
        if isinstance(error,commands.CommandOnCooldown):            
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