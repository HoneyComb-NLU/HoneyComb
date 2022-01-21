from datetime import datetime
from email import header
from urllib import response
import discord
from discord.ext import commands
from discord.commands import slash_command,message_command,user_command
import requests
import utils.osUtils as osu
from requests.structures import CaseInsensitiveDict
import utils.dynamicDictionary as dd

dict_url = "https://owlbot.info/api/v4/dictionary/"

class dictionaey(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @message_command()
    async def meaning(self,ctx, message):
        # await ctx.send(message.content.split(" "))
        word = message.content.split(" ")
        if len(word) == 1:
            word[0] = word[0].replace("-"," ")
            header = CaseInsensitiveDict()
            header["Authorization"] = "Token " + osu.get_dict_key()
            data = requests.get(dict_url+word[0],headers=header)
            response_code = data.status_code
            data = data.json()

            if response_code == 404:
                embed = discord.Embed(
                    title="**Honeycomb Dictionary**",
                    description=f"**No Definition found for word : {word[0]}**",
                    color=discord.Color.red(),
                    timestamp=datetime.now()
                )
                embed.add_field(
                    name="Jump to Message",
                    value=f"[Click here to jump to the message]({message.jump_url})",
                    inline=False
                )
                await ctx.respond(embed=embed)
            
            elif response_code == 200:
                embed = discord.Embed(
                    title="**Honeycomb Dictionary**",
                    description="**" + word[0].capitalize() + "**",
                    color=discord.Color.green(),
                    timestamp=datetime.now()
                )
                for num,each in enumerate(data["definitions"]):
                    if num < 24:
                        embed.add_field(name=each["type"].capitalize(),value=each["definition"].capitalize(),inline=True)
                    else:
                        break

                embed.add_field(
                    name="Jump to Message",
                    value=f"[Click here to jump to the message]({message.jump_url})",
                    inline=False
                )
                await ctx.respond(embed=embed)
                
            elif response_code == 429:
                embed = discord.Embed(
                    title="**Honeycomb Dictionary**",
                    description=f"**Wow! Nice Burnout Bro!**",
                    color=discord.Color.red(),
                    timestamp=datetime.now()
                )
                embed.set_thumbnail(url="https://cdn-icons.flaticon.com/png/512/5282/premium/5282787.png?token=exp=1642744029~hmac=0092920daea3901a6c1b108b3caac739")
                embed.add_field(
                    name="Jump to Message",
                    value=f"[Click here to jump to the message]({message.jump_url})",
                    inline=False
                )
                await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(
                title="**Honeycomb Dictionary**",
                description=f"**Error! Multiple words in This Message**",
                color=discord.Color.red(),
                timestamp=datetime.now()
            )
            embed.add_field(
                name="Jump to Message",
                value=f"[Click here to jump to the message]({message.jump_url})"
            )
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(dictionaey(bot))