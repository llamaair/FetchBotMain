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
        with open("automodguilds.json") as f:
            automodguild = json.load(f)

        if ctx.guild.id not in automodguild:
            automodguild.append(ctx.guild.id)
            await ctx.respond("Enabled automod, saving settings...")
        elif ctx.guild.id in automodguild:
            automodguild.remove(ctx.guild.id)
            await ctx.respond("Disabled automod, saving settings...")

        with open("automodguilds.json", "w+") as f:
            json.dump(automodguild, f)

        await ctx.respond("Settings saved!")

    @commands.Cog.listener()
    async def on_message(self, message):
        banned_words = ["bitch"]
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel.name)
        guild = str(message.guild.name)
        print(f'{username} : {user_message} ({channel}) ({guild})')
        for word in banned_words:
            for word in message.content:
                await message.delete()
                await message.channel.send(f"{message.author.mention}, you just used a banned word, please do not do that again :eyes:")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(automod(bot)) # add the cog to the bot