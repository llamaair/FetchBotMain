import discord
from discord.ext import commands
import asyncio
import time
import random

class tools(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot


    @discord.slash_command(description="Generate a random number")
    async def randnum(self, ctx, lowernumber: int, uppernumber: int):
        number = random.randrange(lowernumber, uppernumber)
        return await ctx.respond(
            f"Your random number in range of {lowernumber} and {uppernumber} is {number}"
    )

    @discord.slash_command(description="Generate a random hex color!")
    async def randomcolor(self, ctx):
        color = discord.Embed(
        title="Your color",
        color=discord.Color.random()
        )
        await ctx.respond(embed=color)

    @discord.slash_command(description="See a users avatar!")
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(title=f"{str(member)}'s avatar :", color = random.randrange(0, 0xffffff)) 
        embed.set_image(url=member.avatar.url)
        embed.set_footer(icon_url = ctx.author.avatar.url,text =f"Requested By {ctx.author}")
        await ctx.respond(embed=embed)

    @discord.slash_command(description="Send a Thanks to another member")
    async def thanks(self, ctx, member: discord.User):
        await ctx.respond("Thanks sent", ephemeral = True)
        await member.send(f"You just recived a thank you from {ctx.author}")

    @discord.slash_command(description="Print info about the servers fetchbot is used in")
    @commands.has_permissions(administrator=True)
    async def servers(self, ctx):
        embed = discord.Embed()
        for guild in self.guilds:
            embed.add_field(name=":crown:", value=guild)
        await ctx.respond(embed = embed)

    @discord.slash_command(description="Do a action that fetchbot will print with your name")
    async def me(self, ctx, *, message):
        await ctx.respond("Successfully performed an action!",ephemeral=True)
        await ctx.send(f"*{ctx.author.mention} {message}*")
        return

    @discord.slash_command(description="Make the bot perform an action")
    @commands.has_permissions(kick_members=True)
    async def botme(self, ctx, *, message):
        await ctx.respond("Successfully performed botme",ephemeral=True)
        await ctx.send(f"*{message}*")

    @discord.slash_command(description="Ping!")
    async def pong(self, ctx):
        await ctx.respond('Pong! {0}'.format(round(bot.latency, 1)))

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(tools(bot)) # add the cog to the bot