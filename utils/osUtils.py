import os
from decouple import config

def get_all_cogs():
    cogList = []
    dir = os.listdir("./cogs/")
    for each in dir:
        if each.endswith(".py"):
            cogList.append((each[:-3]))
    
    return cogList

def get_debug_guilds():
    return list(map(int,config("DEBUG_GUILDS")[1:-1].split(",")))

def get_db():
    return str(config("DB_URL"))    

def get_dict_key():
    return config("DICT_KEY")

def get_NLU_URL():
    return str(config("NLU_URL"))

def get(search_string:str):
    return str(config(search_string))




# BOT_TOKEN
# DEBUG_GUILDS
# DICT_KEY
# DB_URL
# NLU_URL
# DPI