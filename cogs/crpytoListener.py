import asyncio,requests
from pydoc import describe
import discord
from discord.ext import commands
from discord.commands import slash_command,message_command,user_command
import utils.CryptoUtils as cu
import utils.osUtils as osu
import utils.databaseUtils as dbu
from requests.exceptions import HTTPError
import utils.consoleLogger as log


nlu_url = osu.get_NLU_URL()

class cryproListener(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # force_reload_nlu()
        cached_nlu_channels = dbu.get_nlu_channels()
        log.info("Current NLU Channels: " + str(cached_nlu_channels))
        cu.write_coin_list()
        cu.write_supported_currencies()

    @commands.Cog.listener()
    async def on_application_command_error(self,ctx,error):
        log.error(str(error))
        # ------------------------ Error Classification  ------------------------ #
        if isinstance(error, commands.CommandOnCooldown):            
            embed = discord.Embed(
                title="Command Cooldown!",
                description=str(error),
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed,ephemeral=True)

        elif isinstance(error,HTTPError) and str(error)[:3] == "429":
            embed = discord.Embed(
                title="**Wow! Nice Burnout!**",
                description=f"Data request limit exceeded! Please ask <@474589812192575488> to pay for the services. ",
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed,ephemeral=True)
        
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="**Missing permission**",
                description=f"You cannot use this command due to lack of permissions.",
                color=discord.Color.red()
            )
            await ctx.respond(embed=embed,ephemeral=True)

        elif isinstance(error.__context__,AssertionError) or isinstance(error.__context__,KeyError):
            await ctx.respond(embed=discord.Embed(
                title="Token Name Error",
                description="Please input **__Valid__** crypto/exchange id.",
                color=discord.Color.red()
            ),ephemeral=True)
            raise error

        elif isinstance(error.__context__,discord.NotFound):
            await ctx.respond(embed=discord.Embed(
                title="Token Name Error",
                description="Please input **__Valid__** crypto/exchange id.",
                color=discord.Color.red()
            ),ephemeral=True)
        
        elif isinstance(error.__context__,ValueError) and "time data" in str(error):
            await ctx.respond(embed=discord.Embed(
                title="Date Error!",
                description="Please input **__Valid__** Date \n**Accepted Format: ** `DD-MM-YYYY`.",
                color=discord.Color.red()
            ),ephemeral=True)

        elif isinstance(error.__context__,OSError) or isinstance(error.__context__,IndexError):
            await ctx.respond(embed=discord.Embed(
                title="Date Error!",
                description="Please input **__Valid__ & __Sensible__** Date.",
                color=discord.Color.red()
            ),ephemeral=True)


        else:
            await ctx.respond(embed=discord.Embed(
                title="Unexpected Error!",
                description="Please Contact My Developers to get it Fixed!",
                color=discord.Color.red()
            ).add_field(name="<:honeycomb:939792285120483349> HiveMinds Discord Server",value="[Click Here to Join!](https://discord.gg/WSK3wRTYKw)"),
            ephemeral=True)
            await self.bot.get_channel(int(osu.get("CONSOLE"))).send("** "+ ctx.guild.name + " →** `" + str(error) + "`")
            log.error(str(error))
            raise error

    @commands.Cog.listener()
    async def on_message(self,message:discord.Message):
        # ------------------------ Checks ------------------------ #
        if message.author.bot or message.channel.type == discord.ChannelType.private or not dbu.check_nlu_channels(message.channel.id):
            return

        delay_check_fail = message.channel.slowmode_delay < 30
        if delay_check_fail:
            em = discord.Embed(title="Slowmode not detected!",description="""In order to use Natural language mode you will need to have a minimum of 30 seconds slow mode...\n\n*Silently enables slowmode... hehehehe...*""",color=discord.Color.red())
            await message.channel.send(embed=em)
            await message.channel.edit(slowmode_delay=30)
            return
        
        # ------------------------ NLU Resquest ------------------------ #
        resp = requests.post(
            nlu_url,
            json={
                'sender': message.author.id,
                'message': message.content
            }
        ).json()[0]
        # ------------------------ Intent Processing ------------------------ #

        try:
            intent = resp['custom']['intent']['name']
        except KeyError:
            await message.channel.send(resp['text'])
            return -1


        # async with message.channel.typing():    
        if intent == "coin_search":
            await message.channel.send(embed=cu.searching((resp['custom']['slots']['coins'][0])))
        else:
            print("Else Hit!")
        # Smooth Love Potion -> smooth-love-potion




        
def setup(bot):
    bot.add_cog(cryproListener(bot))
