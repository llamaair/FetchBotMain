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
        await ctx.respond('Pong! {0}'.format(round(self.bot.latency, 1)))

    @discord.slash_command(description="Get the server's current boostcount")
    async def boostcount(self, ctx):
        embed = discord.Embed(title = f'{ctx.guild.name}\'s Boost Count', description = f'{str(ctx.guild.premium_subscription_count)}')
        await ctx.respond(embed = embed)

    @discord.slash_command(description="Get a invite link to our support server!")
    async def support(self, ctx):
        await ctx.respond("Have you found an issue with FetchBot or a bug? Join our support server; https://discord.gg/uBEK23mmmK")


    @discord.slash_command(description="Subtract a number from another number!")
    async def subtract(self, ctx, firstnumber:int, secondnumber:int):
        await ctx.respond(f"{firstnumber}-{secondnumber} = {firstnumber-secondnumber}")
    
    @discord.slash_command(description="Get info about the server")
    async def serverinfo(self, ctx):
        id = ctx.guild.id
        txt = len(ctx.guild.text_channels)
        vc = len(ctx.guild.voice_channels)
        tim = str(ctx.guild.created_at)
        owner=ctx.guild.owner
        embed=discord.Embed(
        title=f"Server info"
        )
        embed.add_field(name=":ballot_box: Server Name", value=f"{ctx.guild}")
        embed.add_field(name=":crown: Server Owner", value=owner)
        embed.add_field(name=":calendar: Created at", value=f"{tim}")
        embed.add_field(name="Text Channels", value=f"{txt}")
        embed.add_field(name="Voice Channels", value=f"{vc}")
        embed.add_field(name="ID", value=f"{id}")
        await ctx.respond(embed=embed)

    @discord.slash_command(description="Get info about a member")
    async def whois(self, ctx, member:discord.Member):
        j = str(member.joined_at)[0:11]
        c = str(member.created_at)[0:11]
        embed=discord.Embed(
        title="User Info"
        )
        embed.add_field(name=":name_badge: Name", value=f"{member.name}")
        embed.add_field(name="Nickname", value=f"{member.nick}")
        embed.add_field(name=":flower_playing_cards: Joined Discord", value=f"{c}")
        embed.add_field(name="Joined Server", value=f"{j}")
        embed.add_field(name=":credit_card: ID", value=f"{member.id}")
        embed.add_field(name="Highest role", value=f"{member.top_role.mention}")
        embed.set_footer(text=f"Requested by: {ctx.author.name}")
        await ctx.respond(embed=embed)

    @discord.slash_command(description="Just a calculator")
    async def calculate(self, ctx, operation, number1, number2):
        if operation not in ['+', '-', '*', '/']:
            await ctx.respond('Please type a valid operation type.')
        var = f' {operation} '.join(number1).join(number2)
        await ctx.respond(f'{var} = {eval(var)}')

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(tools(bot)) # add the cog to the bot