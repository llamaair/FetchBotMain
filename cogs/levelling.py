import discord
from discord.ext import commands
import asyncio
import random
import json

class levelling(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('levels.json', 'r') as f:
            users = json.load(f)

        if not f'{member.id}' in users:
            users[f'{member.id}'] = {}
            users[f'{member.id}']['experience'] = 0
            users[f'{member.id}']['level'] = 1

        with open('levels.json', 'r'):
            json.dump(users, f)

    @commands.Cog.listener()
    async def on_message(message):
        if message.author.bot == False:
            with open('users.json', 'r') as f:
                users = json.load(f)

            if not f'{message.author.id}' in users:
                users[f'{message.author.id}'] = {}
                users[f'{message.author.id}']['experience'] = 0
                users[f'{message.author.id}']['level'] = 1
            
            users[f'{levels.id}']['experience'] += 5
            with open('levellling.json', 'r') as g:
                levels = json.load(g)
            experience = users[f'{message.authoe.id}']['experience']
            lvl_start = users[f'{message.author.id}']['level']
            lvl_end = int(experience ** (1 / 4))
            if lvl_start < lvl_end:
                await message.channel.send(f'{message.author.mention} has leveled up to level {lvl_end}')
                users[f'{message.author.id}']['level'] = lvl_end

        with open('users.json', 'w') as f:
            json.dump(users, f)


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(levelling(bot)) # add the cog to the bot