import discord
from pyparsing import Empty
from datetime import datetime

def create_dynamic_embed(json):
    emb = discord.Embed(
        title="Honeycomb Dictionary",
        # description="",
        color=discord.Color.green(),
        timestamp=datetime.now()
    )
    for each in json["definitions"]:
        emb.add_field(name=each["type"].capitalize(),value=each["definition"].capitalize(),inline=True)
    return emb