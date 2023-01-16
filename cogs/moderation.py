import discord
from discord.ext import commands
import asyncio
import time
from datetime import timedelta

class moderation(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot


    @discord.slash_command(description="Ban people")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User, reason="No reason Provided"):
        try:
            await ctx.guild.ban(user, reason=reason)
            await ctx.respond(f"Successfully banned {user.mention} for {reason}!")
            try:
                await user.send(
                f"You have been banned from {ctx.guild} for {reason}!\nBanned by: {ctx.author}"
            )
            except:
                pass
        except Exception as e:
            await ctx.respond(f"Unable to ban that person!")

    @discord.slash_command(description="Kick people")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.User, reason="No reason Provided"):

        try:
            await ctx.guild.kick(user, reason=reason)
            await ctx.respond(f"Successfully kicked {user.mention} for {reason}!")
            try:
                await user.send(
                f"You have been kicked from {ctx.guild} for {reason}!\kicked by: {ctx.author}"
            )
            except:
                pass
        except Exception as e:
            await ctx.respond(f"Unable to kick that person!")

    @discord.slash_command(description="Warn a member")
    @commands.has_permissions(moderate_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason):
        await ctx.respond("Warning sent",ephemeral=True)
        await ctx.send(f"{member.mention}, you have been warned by {ctx.author.mention} for {reason}")

    @discord.slash_command(description="Delete the channel you use the command in")
    @commands.has_permissions(manage_channels=True)
    async def delchannel(self, ctx):
      await ctx.respond("Channel is now being deleted",ephemeral=True)
      await asyncio.sleep(2)
      await ctx.channel.delete()

    @discord.slash_command(description="Delete messages")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.respond("Clearing messages")
        time.sleep(1)
        amount += 1
        await ctx.channel.purge(limit=amount)

    @discord.slash_command(description="Time another member out")
    @commands.has_permissions(moderate_members = True)
    async def timeout(self, ctx, member : discord.Member, time):
        await member.timeout_for(timedelta(minutes=time))
        

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(moderation(bot)) # add the cog to the bot