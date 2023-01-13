import discord
from discord.ext import commands
import asyncio
import random
import json
import datetime
import time
from datetime import timedelta

class automod(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
        self.anti_spam = commands.CooldownMapping.from_cooldown(5, 15, commands.BucketType.member)

    @discord.slash_command(description="Enable or disable automod")
    @commands.has_permissions(administrator = True)
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
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel.name)
        guild = str(message.guild.name)
        with open("automodguilds.json") as f:
            automodguild = json.load(f)
        if message.guild.id in automodguild:
            if 'nigga' in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention} watch your mouth :eyes:")
            if 'foo' in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention} watch your mouth :eyes:")
            if 'motherfucker' in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention} watch your mouth :eyes:")
            if 'nigger' in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention} watch your mouth :eyes:")
            if 'bitch' in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention} watch your mouth :eyes:")
            if 'fucker' in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention} watch your mouth :eyes:")
            if len(message.raw_mentions) > 5:
                await message.delete()
                await message.channel.send(f"{message.author.mention} Please do not mass mention people :skull:")
            if len(message.raw_mentions) > 7:
                await message.author.timeout_for(timedelta(minutes=15))
            if len(message.raw_mentions) > 14:
                await message.author.send(f"You have been banned from {message.guild} for mass mentioning people by FetchBot Automod")
                await message.author.ban(reason = "Mass mentioning")
            bucket = self.anti_spam.get_bucket(message)
            retry_after = bucket.update_rate_limit()
            if retry_after:
                await message.delete()
                await message.channel.send(f"{message.author.mention}, don't spam!", delete_after = 10)
                await message.author.timeout_for(timedelta(minutes=30))


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(automod(bot)) # add the cog to the bot