import discord
from discord.ext import commands
import asyncio
import random
import json

class welcome(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(description="Enable or disable auto welcome")
    @commands.has_permissions(administrator = True)
    async def welcoming(self, ctx):
        with open("welcoming.json") as f:
            automodguild = json.load(f)

        if ctx.guild.id not in automodguild:
            automodguild.append(ctx.guild.id)
            await ctx.respond("Enabled auto welcoming, saving settings...")
        elif ctx.guild.id in automodguild:
            automodguild.remove(ctx.guild.id)
            await ctx.respond("Disabled auto welcoming, saving settings...")

        with open("welcoming.json", "w+") as f:
            json.dump(automodguild, f)

        await ctx.respond("Settings saved!")
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("welcoming.json") as f:
            automodguild = json.load(f)
        if message.guild.id in automodguild:
            if member.guild.system_channel: # If it is not None
                await member.guild.system_channel.send(f'Welcome to {member.guild.name}, {member.mention}. We hope you will enjoy you time here :tada: :tada:')


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(welcome(bot)) # add the cog to the bot