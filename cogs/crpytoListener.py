import asyncio,requests,os
from click import command
from datetime import datetime
import discord
from discord.ext import commands,pages
from discord.commands import slash_command,message_command,user_command
import utils.CryptoUtils as cu
import utils.osUtils as osu
import utils.databaseUtils as dbu
from requests.exceptions import HTTPError
import utils.consoleLogger as log
from dateutil.relativedelta import relativedelta

nlu_url = osu.get_NLU_URL()

class cryproListener(commands.Cog):
    def __init__(self,bot:discord.Bot):
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
        if message.type != discord.enums.MessageType.default or len(message.attachments) != 0:
            return

        if message.author.bot or message.channel.type == discord.ChannelType.private or not dbu.check_nlu_channels(message.channel.id):
            return

        delay_check_fail = message.channel.slowmode_delay < 30
        if delay_check_fail:
            em = discord.Embed(title="Slowmode not detected!",description="""In order to use Natural language mode you will need to have a minimum of 30 seconds slow mode...\n\n*Silently enables slowmode... hehehehe...*""",color=discord.Color.red())
            await message.channel.send(embed=em)
            await message.channel.edit(slowmode_delay=30)
            return
        
        # ------------------------ NLU Resquest ------------------------ #
        async with message.channel.typing():
            try:
                resp = requests.post(
                    nlu_url,
                    json={
                        'sender': message.author.id,
                        'message': message.content
                    }
                ).json()[0]['custom']
            except IndexError:
                try:
                    resp = requests.post(
                    nlu_url,
                    json={
                        'sender': message.author.id,
                        'message': message.content
                    }
                    ).json()[0]
                except IndexError:
                    log.error("No Reply found for :`" + message.content +"`!!")
                    return -1
            # ------------------------ Intent Processing ------------------------ #

            try:
                intent = resp['intent']
            except KeyError:
                await message.channel.send(resp['text'])
                return -1
            
            # async with message.channel.typing():  
            int_list = ["greet", "goodbye", "affirm", "deny" ,"mood_great", "mood_unhappy","bot_challenge", "need_help", "chit_chat", "nlu_fallback"]  
            if intent in int_list:
                await message.channel.send(resp['responses'])
                
            elif intent == "coin_search":
                await message.channel.send(embed=cu.searching(resp['slots']['coins'][0]))
            elif intent == "coin_data":
                # if resp['slots']['currencies'] == []:
                #     curr = None
                # else:
                #     curr = ",".join(resp['slots']['currencies'])#[1:-1]
                
                # resPaginator = pages.Paginator(
                #     pages=list(cu.page_coin_details(guild_id=message.guild.id,id=resp['slots']['coins'][0],vs_currency=curr)),
                #     timeout=60,
                #     show_disabled=True,
                #     show_indicator=True,
                #     use_default_buttons=False,
                #     custom_buttons=cu.get_Paginator_buttons()
                # )
                # ctx = await self.bot.get_context(message)
                # await resPaginator.send(self.bot.get_application_context(message.interaction))
                await message.channel.send("Develops are still working on bringing this feature for `NLU` mode, This is because the Paginator we provide doesn't support stand-alone operation yet.\n Until we work on bringing this feature to life, You can use `/coin_data` for the same! ")
                

            elif intent == "simple_coin_price":
                if resp['slots']['currencies'] == []:
                    curr = None
                else:
                    curr = ",".join(resp['slots']['currencies'])#[1:-1]
                
                coins = ",".join(resp['slots']['coins'])
                
                await message.channel.send(
                    embed=cu.get_price(
                        message.guild.id,
                        coins,
                        curr
                    )
                )
            elif intent == "chart":
                
                if resp['slots']['chart_type'] != 'ohlc':
                    #Normal + ranged classifier
                    if resp['slots']['time'] == {}:
                        embed,imgFile,imgName=cu.make_normal_chart(
                            coin_id=resp['slots']['coins'][0],
                            vs_curr=resp['slots']['currencies'][0] if len(resp['slots']['currencies'])!= 0 else None,
                            days = '1',type=resp['slots']['chart_type'],
                            user_id=message.author.id,guild_id=message.guild.id
                        )
                        await message.channel.send(file=imgFile,embed=embed)

                    elif type(resp['slots']['time']['to']) == None or type(resp['slots']['time']) == str:
                        from_time = datetime.strptime(resp['slots']['time'][:-10],"%Y-%m-%dT%H:%M:%S")
                        to_time = datetime.now()
                        rldt = relativedelta(to_time,from_time)
                        time = str(rldt.days)

                        embed,imgFile,imgName=cu.make_normal_chart(
                            coin_id=resp['slots']['coins'][0],
                            vs_curr=resp['slots']['currencies'][0] if len(resp['slots']['currencies'])!= 0 else None,
                            days=time,type=resp['slots']['chart_type'],
                            user_id=message.author.id,guild_id=message.guild.id
                        )

                        await message.channel.send(file=imgFile,embed=embed)

                    else: 
                        from_time = datetime.strptime(resp['slots']['time']['from'][:-10],"%Y-%m-%dT%H:%M:%S").timestamp()
                        to_time = datetime.strptime(resp['slots']['time']['to'][:-10],"%Y-%m-%dT%H:%M:%S").timestamp()
                        embed,imgFile,imgName=cu.make_ranged_chart(
                                coin_id=resp['slots']['coins'][0],
                                vs_curr=resp['slots']['currencies'][0] if len(resp['slots']['currencies'])!= 0 else None,
                                from_timedelta=from_time,to_timedelta=to_time,
                                type=resp['slots']['chart_type'],
                                user_id=message.author.id,guild_id=message.guild.id
                            )
                        await message.channel.send(file=imgFile,embed=embed)
                      
                elif resp['slots']['chart_type'] == 'ohlc':
                    #Ohlc caller
                    from_time = datetime.strptime(resp['slots']['time']['from'][:-10],"%Y-%m-%dT%H:%M:%S")
                    to_time = datetime.strptime(resp['slots']['time']['to'][:-10],"%Y-%m-%dT%H:%M:%S")
                    rldt = relativedelta(to_time,from_time)
                    time = str(rldt.days)
                    # print(">>> "+ time)
                    embed,imgFile,imgName=cu.make_ohlc_chart(
                        coin_id=resp['slots']['coins'][0],
                        vs_curr=resp['slots']['currencies'][0] if len(resp['slots']['currencies'])!= 0 else None,
                        days=time,
                        user_id=message.author.id,guild_id=message.guild.id
                    )
                    await message.channel.send(file=imgFile,embed=embed)

                    pass
                else:
                    log.error("Chart Type Mismatch!")


                await asyncio.sleep(2)
                os.remove(f"./charts/{imgName}.png")
            
            else:
                await message.channel.send("Sorry, I am unable to get what you are saying! :(")

        # Smooth Love Potion -> smooth-love-potion


        
def setup(bot):
    bot.add_cog(cryproListener(bot))
