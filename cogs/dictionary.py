from datetime import datetime
from email import header
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
    async def meaning(self,ctx, message: discord.Message):
        # await ctx.send(message.content.split(" "))
        word = message.content.split(" ")
        if len(word) == 1:
            header = CaseInsensitiveDict()
            header["Authorization"] = "Token " + osu.get_dict_key()
            data = requests.get(dict_url+word[0],headers=header)
            data = data.json()
            
            # print(osu.get_dict_key())
            
            embed = discord.Embed(
                title="Honeycomb Dictionary",
                # description="",
                color=discord.Color.green(),
                timestamp=datetime.now()
            )
            for each in data["definitions"]:
                embed.add_field(name=each["type"].capitalize(),value=each["definition"].capitalize(),inline=True)
            
            embed.add_field(
                name="Jump to Message",
                value=f"[Click here to jump to the message]({message.jump_url})",
                inline=False
            )
            
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(
                title="Dictionary",
                description=f"Error! Multiple words in This Message",
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