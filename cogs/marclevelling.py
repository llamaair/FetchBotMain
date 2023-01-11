import discord
from discord.ext import commands
import asyncio
import random
import json

class fun(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(message):
        if message.author.bot == False:
            with open('levels.json', 'r') as f:
                users = json.load(f)

            if not f'{message.author.id}' in users:
                users[f'{message.author.id}'] = {}
                users[f'{message.author.id}']['experience'] = 0
                users[f'{message.author.id}']['level'] = 1

            


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(fun(bot)) # add the cog to the bot