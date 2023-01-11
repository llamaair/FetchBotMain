import discord
from discord.ext import commands
import asyncio
import random
import json

class automod(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(description="Activate a premium subscription with a code")
    async def automod(self, ctx):
        authorr = ctx.author
        with open("automodguilds.json") as f:
            autmodguild = json.load(f)

        if guild.id not in automodguild:
            automodguild.append(ctx.guild.id)
            await ctx.respond("Enabled automod, saving settings...")
        elif guild.id in automodguild:
            automodguild.remove(ctx.guild.id)
            await ctx.respond("Disabled automod, saving settings...")

        with open("automodguilds.json", "w+") as f:
            json.dump(codes_list, f)

        await ctx.respond("Settings saved!")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(automod(bot)) # add the cog to the bot