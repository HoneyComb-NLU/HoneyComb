import discord
import utils.osUtils as osu
from discord.commands import slash_command,message_command,user_command
from discord.commands import Option
from discord.ext import commands
import random

dgid = osu.get_debug_guilds()

class Guess_Tick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command()
    async def guess(self, ctx, number: Option(int, description="Your Guessed number.",required=True)):
        # val = random.randrange(1,5)
        val = 1
        if (number == val):
            await ctx.respond("ok")
            # await msg.add_reaction(emoji)

    @slash_command()
    async def wtf(self, ctx):
        await ctx.respond()
        emoji = "\N{WHITE HEAVY CHECK MARK}" 
        msg = await ctx.send("Hmmmk....")
        await msg.add_reaction(emoji)

def setup(bot):
    bot.add_cog(Guess_Tick(bot))