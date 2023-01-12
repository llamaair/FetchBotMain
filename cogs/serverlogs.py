import discord
from discord.ext import commands
import asyncio
import random

class serverlogs(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        guild=message.author.guild
        author = message.author
        ch = message.channel
        content = message.content
        orange = discord.Color.dark_orange()
        for channel in guild.channels:
            if str(channel.name) == "server-logs":
                msg_del = str(f"{content}")
                aut_name= str(f"{author.display_name}")
                ch_name = str(f"{ch.name}")
                embed = discord.Embed(color=orange)
                embed.set_author(name="Message Deleted")
                embed.add_field(name=f"Message", value=msg_del, inline=False)
                embed.add_field(name=f"Message Author", value=aut_name, inline=False)
                embed.add_field(name=f"Channel", value=ch_name, inline=False)
                await channel.send(embed=embed)


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(serverlogs(bot)) # add the cog to the bot