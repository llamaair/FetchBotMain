import discord
import asyncio
import random
import datetime
import time
import string
from discord.ext import commands
from discord.ext import tasks
import os
import json
from discord.ext.commands import check
from dotenv import load_dotenv

#---------------------------#
#NAME: FetchBot
#Status: Working
#Version: 3.0.0
#Creator: Marc13 and Raxeemo
#---------------------------#
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()

client = discord.Bot(intents=intents, help_command=None)

#Defining startup
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="/help"))
    global startTime
    startTime = time.time()

@client.event
async def on_message(message):
  username = str(message.author)
  user_message = str(message.content)
  channel = str(message.channel.name)
  guild = str(message.guild.name)
  print(f'{username} : {user_message} ({channel}) ({guild})')
    

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.respond("You don't have the required permissions to run this command!")
  if isinstance(error, commands.CommandOnCooldown):
    retry_after = int(error.retry_after)
    await ctx.respond(f"This command is on cooldown! Try again in {retry_after} seconds!")

def check_if_user_has_premium(ctx):
  with open("premium_users.json") as f:
    premium_users_list = json.load(f)
    if ctx.author.id not in premium_users_list:
      return False

  return True


@client.command(aliases=['h'], description="Get a list of commands!")
async def help(ctx):
    helpem = discord.Embed(
        title="✦Help✦",
        description="**Please DM Me If you Found Any Problems : Marc13#1627**",
        color=discord.Color.random())

    helpem.add_field(
        name=":red_circle: Main commands :red_circle:",
        value=
        "**/randnum\n/help\n/kick\n/ban\n/clear\n/dog\n/cat\n/fatcat\n/fatdog\n/giveaway\n/fact\n/manga\n/anime\n/membercount\n/invite\n/creroll\n/champion\n/alimit\n/flush\n/flushnick\n/future\n/reroll\n/rps\n/react\n/servers\n/info\n/me\n/ask\n/threat\n/warn\n/stupid\n/smart\n/delchannel\n/uptime\n/abuse\n/challenge\n/whois\n/avatar\n/helpmember**"
    )

    helpem.add_field(
      name=":family_woman_boy: Relation commands :family_woman_boy:",
      value=

      "**/createaccount\n/relation\n/clearaccount\n/pet**"
    )

    helpem.add_field(
      name=":coin: Premium commands :coin:",
      value=

      "**/ping\n/imagesearch\n/createday\n/poll\n/shortening\n/pron\n/unlock\n/lock\n/announce\n/github\n/spotify\n/meme\n/comic\n/slowmode**"
    )

    helpem.add_field(
      name=":moneybag: Economy commands :moneybag:", value=

"**/balance\n/memberbalance\n/inventory\n/memberinventory\n/beg\n/daily\n/shop\n/buy\n/rob\n/pay\n/deposit\n/withdraw\n/set**"
    )


    helpem.set_footer(text=f"Requested By {ctx.author.name}",
                      icon_url=ctx.author.avatar.url)

    helpem.set_author(name=client.user.name, icon_url=client.user.avatar.url)

    return await ctx.respond(embed=helpem)

@client.command(description="Send help to a member!")
@commands.has_permissions(manage_guild=True)
async def helpmember(ctx,member:discord.Member):
  helpem = discord.Embed(
    title="✦Help✦",
    description="**Please DM Me If you Found Any Problems : Marc13#1627**",
    color=discord.Color.random())

  helpem.add_field(
    name=":red_circle: Main commands :red_circle:",
    value=
        "**/randnum\n/help\n/kick\n/ban\n/clear\n/dog\n/cat\n/fatcat\n/fatdog\n/giveaway\n/fact\n/manga\n/anime\n/membercount\n/invite\n/creroll\n/champion\n/alimit\n/flush\n/flushnick\n/future\n/reroll\n/rps\n/react\n/servers\n/info\n/me\n/ask\n/threat\n/warn\n/stupid\n/smart\n/delchannel\n/uptime\n/abuse\n/challenge\n/whois\n/avatar**"
    )

  helpem.add_field(
    name=":family_woman_boy: Relation commands :family_woman_boy:",
    value=

      "**/createaccount\n/relation\n/clearaccount\n/pet**"
    )

  helpem.add_field(
    name=":coin: Premium commands :coin:",
    value=

      "**/ping\n/imagesearch\n/createday\n/poll\n/shortening\n/pron\n/unlock\n/lock\n/announce\n/github\n/spotify\n/meme\n/comic\n/slowmode**"
    )


  helpem.set_footer(text=f"Requested By {ctx.author.name}",
  icon_url=ctx.author.avatar.url)

  helpem.set_author(name=client.user.name, icon_url=client.user.avatar.url)

  await ctx.respond("Help sent!",ephemeral=True)
  return await member.send(embed=helpem)
  

@client.command(description="Generate a random number")
async def randnum(ctx, lowernumber: int, uppernumber: int):
    number = random.randrange(lowernumber, uppernumber)
    return await ctx.respond(
        f"Your random number in range of {lowernumber} and {uppernumber} is {number}"
    )

@client.command(description="Generate a random hex color!")
async def randomcolor(ctx):
  color = discord.Embed(
    title="Your color",
    color=discord.Color.random()
  )
  await ctx.respond(embed=color)

@client.command(description="See a users avatar!")
async def avatar(ctx, *, member: discord.Member = None):
  if member == None:
    member = ctx.author
  embed = discord.Embed(title=f"{str(member)}'s avatar :", color = random.randrange(0, 0xffffff)) 
  embed.set_image(url=member.avatar.url)
  embed.set_footer(icon_url = ctx.author.avatar.url,text =f"Requested By {ctx.author}")
  await ctx.respond(embed=embed)

@client.command(aliases=['Gw'], description="Host a giveaway")
@commands.has_permissions(administrator=True)
async def giveaway(ctx):
    await ctx.respond(
        "Hello . Please answer to these questions within 15 Seconds to Start the giveaway."
    )

    await asyncio.sleep(2)

    questions = [
        "Please mention the channel to host the giveaway : ",
        "What should be the duration of the giveaway? (1s,1m,1h,1d,...)",
        "What is the prize of this giveaway?"
    ]
    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.respond(i)
        try:
            msg = await client.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(
                'You didn\'t answer in time, please be quicker next time!')
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])

    except:
        await ctx.send(
            f"You didn't mention a channel properly . Do it like this {ctx.channel.mention} ."
        )
        return

    channel = client.get_channel(c_id)
    time = convert(answers[1])
    if time == -1:
        await ctx.send(
            f"You didn't answer the time with a proper unit . Use (S|M|H|D) . Ex : 5m ( 5 Minutes )"
        )
        return
    elif time == -2:
        await ctx.send("Time must be a number !")
        return
    prize = answers[2]

    await ctx.send(
        f"The giveaway will be in {channel.mention} and will last for {answers[1]} ."
    )

    embed = discord.Embed(title=":tada: **Giveaway!** :tada:",
                          description=f"{prize}",
                          color=ctx.author.color)
    embed.add_field(name="Hosted by:", value=ctx.author.mention)
    embed.set_footer(text=f"Ends in {answers[1]} !")
    my_msg = await channel.send(embed=embed)

    await my_msg.add_reaction("🎉")
    await asyncio.sleep(time)
    try:
        new_msg = await channel.fetch_message(my_msg.id)
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(client.user))
        winner = random.choice(users)

        await channel.send(f"Congratulations! {winner.mention} won {prize}!")
    except:
        await channel.send(
            "Giveaway ended and there were no winners because nobody reacted :pensive:"
        )
        return


def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}
    unit = time[-1]
    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]





@client.command(description="Get a cute cat picture")
async def cat(ctx):
    catlinks = [
        'https://images.unsplash.com/photo-1591871937573-74dbba515c4c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8NHx8fGVufDB8fHx8&w=1000&q=80',
        'https://i.guim.co.uk/img/media/26392d05302e02f7bf4eb143bb84c8097d09144b/446_167_3683_2210/master/3683.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=49ed3252c0b2ffb49cf8b508892e452d',
        'https://th-thumbnailer.cdn-si-edu.com/bZAar59Bdm95b057iESytYmmAjI=/1400x1050/filters:focal(594x274:595x275)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer/95/db/95db799b-fddf-4fde-91f3-77024442b92d/egypt_kitty_social.jpg',
        'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/best-girl-cat-names-1606245046.jpg?crop=0.668xw:1.00xh;0.126xw,0&resize=640:*',
        'https://i.pinimg.com/736x/9f/01/73/9f01736a2bd0986452bd95ef05abf425.jpg',
        'https://i.ytimg.com/vi/YSHDBB6id4A/maxresdefault.jpg',
        'https://images.unsplash.com/photo-1574144611937-0df059b5ef3e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZnVubnklMjBjYXR8ZW58MHx8MHx8&w=1000&q=80',
        'https://i0.wp.com/katzenworld.co.uk/wp-content/uploads/2019/06/funny-cat.jpeg?fit=1920%2C1920&ssl=1'
    ]
    catchoice = random.choice(catlinks)
    await ctx.respond(catchoice)


@client.command(description="Get a cute dog picture")
async def dog(ctx):
    await ctx.respond(
        "https://i.natgeofe.com/n/3faa2b6a-f351-4995-8fff-36d145116882/domestic-dog_16x9.jpg"
    )


@client.command(description="Get a picture of a fat cat!")
async def fatcat(ctx):
    await ctx.respond(
        "https://live.staticflickr.com/3652/3513292420_6becf54bbf.jpg")


@client.command(description="Get a picture of a fat dog!")
async def fatdog(ctx):
    fatdoglist = [
        "https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Fmobile%2F000%2F029%2F671%2Fwide_dog_cover2_.jpg",
        "https://s.abcnews.com/images/Entertainment/HT_vincent4_dog_ml_160413_16x9_608.jpg"
    ]
    fatdogchoise = random.choice(fatdoglist)
    await ctx.respond(fatdogchoise)


@client.command(aliases=['purge', 'delete'], description="Delete messages")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.respond("Clearing messages")
    time.sleep(1)
    amount += 1
    await ctx.channel.purge(limit=amount)


@client.command(description="Print a random fact")
async def fact(ctx):
    factlinks = [
        'Rubber bands last longer when refrigerated.',
        'No number from one to 999 includes the letter “a” in its word form.',
        'Edgar Allan Poe married his 13-year-old cousin.',
        'Flamingos can only eat with their heads upside down.',
        'There are 32 muscles in a cat’s ear.',
        'Junk food is as addictive as drugs.',
        'In most advertisements, including newspapers, the time displayed on a watch is 10:10.',
        'A cubic inch of human bone can bear the weight of five standard pickup trucks.',
        'Four out of five children recognize the McDonald’s logo at three years old.',
        'It’s impossible to tickle yourself.',
        'It’s impossible for you to lick your own elbow.',
        'Oreo has made enough cookies to span five back and forth trips to the moon.',
        'Due to a genetic defect, cats can’t taste sweet things.',
        'The average American spends about 2.5 days a year looking for lost items.',
        'If you plug your nose, you can’t tell the difference between an apple, a potato, and an onion.',
        'Somali pirates have such a hatred for Western culture, that the British Navy uses music from Britney Spears to scare them off.',
        'The country of Russia is bigger than Pluto.',
        'Many oranges are actually green.',
        'Playing dance music can help ward off mosquitoes.'
    ]
    factlinkchosen = random.choice(factlinks)
    await ctx.respond(factlinkchosen)


@client.command(description="Send a reboot reminder")
@commands.is_owner()
async def rebootmsg(ctx):
  await ctx.send("**PERFORMING A PLANNED REBOOT**")


@client.command(description="Get a anime picture")
async def anime(ctx):
    animelist = [
        "https://cdn.vox-cdn.com/thumbor/I7I0t87KZ-vf_GSWrH118jwl6d0=/1400x0/filters:no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/23437452/The_Spy_x_Family_Anime_Succeeds_Because_of_Its_Characters_.jpg",
        "https://androspel.com/wp-content/uploads/2022/03/anime-dimensions-tier-list.jpg",
        "https://www.gamespot.com/a/uploads/screen_kubrick/1732/17320263/4019145-anime-dek-image.jpg"
    ]
    animechoise = random.choice(animelist)
    await ctx.respond(animechoise)


@client.command(description="Get a manga picture")
async def manga(ctx):
    mangalist = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Figure_in_Manga_style_pattern.png/190px-Figure_in_Manga_style_pattern.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Manga.png/220px-Manga.png",
        "https://en.canson.com/sites/default/files/styles/large/public/medias-images/manga-007.jpg?itok=NxaBiaif"
    ]
    mangachoice = random.choice(mangalist)
    await ctx.respond(mangachoice)


@client.command(aliases=["mc", "members"],
                description="Get the current membercount in this server")
async def membercount(ctx):

    a = ctx.guild.member_count
    b = discord.Embed(title=f"Members in {ctx.guild.name}",
                      description=a,
                      color=discord.Color((0xffff00)))
    await ctx.respond(embed=b)


@client.command(description="Send a invite link for FetchBot")
async def invite(ctx):
    await ctx.respond(
        "You can invite FetchBot here: https://discord.com/api/oauth2/authorize?client_id=935860231051829258&permissions=8&scope=bot"
    )


@client.command(description="Send a update ping about a new FetchBot version")
@commands.is_owner()
async def update(ctx, pings, version):
    await ctx.send(
        f"{pings}, A new version of FetchBot is now out, Version; {version}!")


@client.command(description="Send a random food picture.")
async def food(ctx):
    foodlist = [
        'https://images.immediate.co.uk/production/volatile/sites/30/2020/08/chorizo-mozarella-gnocchi-bake-cropped-9ab73a3.jpg',
        'https://images.pexels.com/photos/2097090/pexels-photo-2097090.jpeg?cs=srgb&dl=pexels-julie-aagaard-2097090.jpg&fm=jpg',
        'https://prod-wolt-venue-images-cdn.wolt.com/5b99008d49345c000cd430fe/9ba7390e-6609-11eb-8a69-c24ba943a9d3_lingon_food_and_friends_menu_02.jpg'
    ]
    foodchoice = random.choice(foodlist)
    await ctx.respond(foodchoice)


@client.command(description="Send a alimit")
async def alimit(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(
        "----------------------------------------------------------------------------------------"
    )


@client.command(description="Send a Arsenal Logo picture")
async def champion(ctx):
    await ctx.respond(
        "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Arsenal_FC.svg/1200px-Arsenal_FC.svg.png"
    )


@client.command(description="Create a new role")
@commands.has_permissions(manage_roles=True)
async def creroll(ctx, *, name):
    guild = ctx.guild
    await guild.create_role(name=name)
    await ctx.respond(f'The role `{name}` has now been created!')


@client.command(pass_context=True, description="Change a member's nick")
@commands.has_permissions(moderate_members=True)
async def flushnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.respond(f'{member.mention}s nick is now flushed and updated')


@client.command(pass_context=True, description="Reset a member's nick")
@commands.has_permissions(moderate_members=True)
async def flush(ctx, member: discord.Member):
    await member.edit(nick='flushed_nick')
    await ctx.respond(f'Flushed nick for {member.mention}')


@client.command(aliases=['fu'], description="Predict your future")
async def future(ctx):
    futurelist = [
        'You will become poor and homeless',
        'You are going to become rich, and develop a genious tool for Pc;s',
        'You are going to have a decent job that pays a decent ammount of money',
        'You are going to live untill you get 150 years!'
    ]
    future = random.choice(futurelist)
    await ctx.respond(future)


@client.command(aliases=["Thankyou", "Thank you"],
                description="Send a Thanks to another member")
async def thanks(ctx, member: discord.User):
    await ctx.respond("Thanks sent")
    await member.send(f"You just recived a thank you from {ctx.author}")


@client.command(description="Reroll a giveaway")
@commands.has_permissions(administrator=True)
async def reroll(ctx, channel: discord.TextChannel, id_):
    if channel == None:
        await ctx.respond("Please mention a channel.")
        return
    if id_ == None:
        await ctx.respond("Please enter the giveaway's ID.")
        return
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.respond("The id was entered incorrectly.")
        return

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! The new winner is {winner.mention}!")


@client.command(description="Play rock, paper, scissors!")
async def rps(ctx, *, player_choice):
    username = str(ctx.author).split('#')[0]
    if player_choice == None:
        await ctx.respond("Please enter rock, paper or scissors .")
        return
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)
    if player_choice.lower() not in choices:
        await ctx.respond('Please enter rock , paper or scissors .')
    else:
        if player_choice.lower() == bot_choice.lower():
            await ctx.respond(f'Tie . we both picked {bot_choice}')
            return
        elif (player_choice.lower() == 'rock' and bot_choice.lower()
              == 'scissors') or (player_choice.lower() == 'scissors'
                                 and bot_choice.lower() == 'paper') or (
                                     player_choice.lower() == 'paper'
                                     and bot_choice.lower() == 'rock'):
            await ctx.respond(
                f'Yes ! You won , Haha , my choice was {bot_choice}.')
            return
        elif (player_choice.lower() == 'rock' and bot_choice.lower() == 'paper'
              ) or (player_choice.lower() == 'scissors' and bot_choice.lower()
                    == 'rock') or (player_choice.lower() == 'paper'
                                   and bot_choice.lower() == 'scissors'):
            await ctx.respond(
                f"Hey {username} ! Don't be mad but i won . my choice was {bot_choice}."
            )


@client.command(description="Echo a message")
@commands.has_permissions(administrator=True)
async def echo(ctx, *, message):
    if message == None:
        await ctx.respond("Please enter a message to echo.")
    if ctx.author == client.user:
        return
    await ctx.respond("Successfully performed echo",ephemeral=True)
    await ctx.send(message)
    return


@client.command(description="Print info about the servers fetchbot is used in")
@commands.has_permissions(administrator=True)
async def servers(ctx):
    for guild in client.guilds:
        await ctx.respond(guild.name)


@client.command(
    description=
    "React fast with the right emoji to win! Choose between hard and easy")
async def react(ctx, difficulty):
    if difficulty == None:
        await ctx.respond(
            "Please choose the difficulty (easy/hard) Ex : ?react hard.")
        return
    possible = ["hard", "easy"]
    if difficulty.lower() not in possible:
        await ctx.respond("Please choose from hard or easy !")
        return

    await ctx.send("Sending the message (React on the shown emoji to win!) ..."
                   )
    easylist = ["🙂", "😋", "😝", "😀", "😃", "😏", "😩", "🥺", "🧐"]
    hardlist = ["🙁", "😕", "☹️", "😞", "😔", "😠", "😟", "😦", "😧"]
    choosenlist = (hardlist if difficulty == "hard" else easylist)
    emoji = random.choice(choosenlist)
    number = 0
    for i in choosenlist:
        if i != emoji:
            number += 1
        elif i == emoji:
            break

    new_msg = await ctx.send(f"React with {emoji} in 3 seconds !")
    for i in choosenlist:
        await new_msg.add_reaction(i)

    channel = ctx.channel
    the_msg = await channel.fetch_message(new_msg.id)
    users = await the_msg.reactions[number].users().flatten()

    users.pop(users.index(client.user))
    if ctx.author in users:
        await ctx.respond("Well played! You won!")
        return
    await ctx.respond("You didn't react in time!")
    return
    print(users)

@client.command(description="Do a action that fetchbot will print with your name")
async def me(ctx, *, message):
    if ctx.author == client.user:
        return
    await ctx.respond("Successfully performed an action!",ephemeral=True)
    await ctx.send(f"*{ctx.author.mention} {message}*")
    return

@client.command(description="Make the bot perform an action")
@commands.has_permissions(kick_members=True)
async def botme(ctx, *, message):
  await ctx.respond("Successfully performed botme",ephemeral=True)
  await ctx.send(f"*{message}*")

  
@client.command(description="Threaten a member")
async def threat(ctx, member: discord.Member, *, threat):
  await ctx.respond(f"{member}, {ctx.author.mention} says he threatens to {threat}")


@client.command(description="Ask me a question!")
async def ask(ctx, *, question):
  responselist=['Yes', 'No', 'Maybe', 'Sure!', 'Of course!', 'Why not', 'I am tired! Ask me later instead.', 'I have no idea', 'Stupid humans...']
  response = random.choice(responselist)
  await ctx.respond(response)

@client.command(description="How stupid are you?")
async def stupid(ctx):
  stupidlist=['100%', '39%', '0%', '50%', '70%', '20%', '95%', '13%']
  stupidity= random.choice(stupidlist)
  await ctx.respond(f"You are {stupidity} stupid")


@client.command(description="Send a message to a user")
@commands.has_permissions(moderate_members=True)
async def msg(ctx,member : discord.Member,*,message):
  await member.send(message)
  await ctx.respond("Message sent!",ephemeral=True)

@client.command(description="Host a FetchRoyale game")
async def fetchroyale(ctx):
  await ctx.respond("Starting FetchRoyale game!",ephemeral=True)
  startmsg = await ctx.send(f"{ctx.author.mention} is hosting a FetchRoyale game! React below to join! The game will start in 1 minute.")
  startmsg = await startmsg.add_reaction("⚔️")
  await asyncio.sleep(5)
  await ctx.send("**FetchRoyale is now about to start!**")
      
@client.command(description="How smart are you?")
async def smart(ctx):
  smartlist=["0%", "100%", "50%", "20%", "67%"]
  smart = random.choice(smartlist)
  await ctx.respond(f"You are {smart} smart!")


@client.command(description="See how long the bot has been up for")
async def uptime(ctx):
  uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
  await ctx.respond(f"The Bot has been up for {uptime}")


@client.command(description="Add FetchBot Premium to a member")
@commands.is_owner()
async def addpremium(ctx, user : discord.Member):
  with open("premium_users.json") as f:
    premium_users_list = json.load(f)

  if user.id not in premium_users_list:
    premium_users_list.append(user.id)

  with open("premium_users.json", "w+") as f:
    json.dump(premium_users_list, f)

  await ctx.respond(f"{user.mention} has been added to premium!")

@client.command(description="Remove Premium from a member")
@commands.is_owner()
async def removepremium(ctx, user : discord.Member):

  with open("premium_users.json") as f:
    premium_users_list = json.load(f)

  if user.id in premium_users_list:
    premium_users_list.remove(user.id)
  else:
    await ctx.respond(f"{user.mention} is not in the premium users list, so they cannot be removed!")
    return

  with open("premium_users.json", "w+") as f:
    json.dump(premium_users_list, f)

  await ctx.respond(f"{user.mention} has been removed!")

@client.command(description="Get a random challenge!")
async def challenge(ctx):
  challengelist=["Eat a hamburger in 20 seconds", "Say yeet in your most southern accent", "Don't speak today", "Stop watching TV", "Eat slower today", "Do 15 sit-ups", "Learn to draw a face", "Don't drink soda today", "Do something you are scared of", "Abuse FetchBot"]
  challenge = random.choice(challengelist)
  await ctx.respond(challenge)



@client.command(description="Abuse someone!")
async def abuse(ctx, user:discord.Member):
  if user.bot:
    randlist=[f"kills {ctx.author.mention}", f"kicks {ctx.author.mention} out of the server", f"eats {ctx.author.mention}", f"abuses {ctx.author.mention}", f"eyes {ctx.author.mention} slowly"]
    randresponse=random.choice(randlist)
    await ctx.respond(f"*{randresponse}*")
  else:
    await ctx.respond(f"*{ctx.author} abuses {user}*")


@client.command(description="Use + to calculate something!")
async def calculate(ctx, firstnumber:int, secondnumber:int):
  await ctx.respond(f"{firstnumber}+{secondnumber} = {firstnumber+secondnumber}")

@client.command(description="Get info about the server")
async def serverinfo(ctx):
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

@client.command(description="Get info about a member")
async def whois(ctx, member:discord.Member):
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

@client.command(description="Get the server's current boostcount")
async def boostcount(ctx):
    embed = discord.Embed(title = f'{ctx.guild.name}\'s Boost Count', description = f'{str(ctx.guild.premium_subscription_count)}')
    await ctx.respond(embed = embed)

@client.command(description="Get a invite link to our support server!")
async def support(ctx):
  await ctx.respond("Have you found an issue with FetchBot or a bug? Join our support server; https://discord.gg/uBEK23mmmK")


@client.command(description="Subtract a number from another number!")
async def subtract(ctx, firstnumber:int, secondnumber:int):
  await ctx.respond(f"{firstnumber}-{secondnumber} = {firstnumber-secondnumber}")

@client.command(description="Pull the latest version from github and restart the bot")
@commands.is_owner()
async def gitpull(ctx):
  await ctx.respond("Pulling from git and restarting",ephemeral=True)
  await ctx.send("**Performing a planned github pull and restarting**")
  quit()


@client.command(description="Get information about FetchBot Premium")
async def premium(ctx):
  await ctx.respond("FetchBot Premium gives you access to a whole lot of new commands, aswell as more features! You can find the list with premium commands at the command; /help")

@client.command(description="Ping!")
async def pong(ctx):
  await ctx.respond('Pong! {0}'.format(round(client.latency, 1)))

@client.command(description="See if you have premium!")
@check(check_if_user_has_premium)
async def premiumstatus(ctx):
  await ctx.respond("You are a premium user!")

@client.command(description="Get a comic!")
@check(check_if_user_has_premium)
async def comic(ctx):
  chosen = random.randint(1,1500)
  await ctx.respond(f"https://xkcd.com/{chosen}")

@client.command(description="Post a meme!")
@check(check_if_user_has_premium)
async def meme(ctx):
  memelist=["https://img.delicious.com.au/WqbvXLhs/del/2016/06/more-the-merrier-31380-2.jpg", "https://pd-beamliving-cd.beamliving.com/-/media/bu-to-ch/cat-meme-netflix-funny-1000x666.png", "https://new.boredteachers.com/wp-content/uploads/2021/04/memes.jpg", "https://i.chzbgr.com/thumb800/18939909/h4090C4E2/memes-animal-memes-funny-animal-memes-memes-funny-memes-funny-cute-cute-animals-cute-animal-memes", "https://i.chzbgr.com/thumb800/18935045/h61FAABB3/and-claimed-my-dad-as-his-person-yes-that-is-a-picture-of-his-cat-on-his-comforter-umicroducklett"]
  meme = random.choice(memelist)
  await ctx.respond(meme)

@client.command(description="Send a announcement using the bot!")
@commands.has_permissions(administrator=True)
@check(check_if_user_has_premium)
async def announce(ctx,announcement):
  embed=discord.Embed(
    title=f"{announcement}"
  )
  await ctx.channel.send(embed=embed)
  await ctx.respond("Successfully sent announcement!",ephemeral=True)

@client.command(description="Get a link to the FetchBot website")
async def website(ctx):
  await ctx.respond("https://marcusolsson123.wixsite.com/fetchbot")

@client.command(description="Lock a channel!")
@commands.has_permissions(manage_channels=True)
@check(check_if_user_has_premium)
async def lock(ctx, channel : discord.TextChannel):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = False
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  await ctx.respond('Channel locked.')

@client.command(description="Unlock a channel!")
@commands.has_permissions(manage_channels=True)
@check(check_if_user_has_premium)
async def unlock(ctx, channel : discord.TextChannel):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = True
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  await ctx.respond('Channel unlocked.')

@lock.error
async def lock_error(ctx, error):
  if isinstance(error,commands.CheckFailure):
    await ctx.respond('You do not have permission to use this command!')

@client.command(description="Start a poll")
@check(check_if_user_has_premium)
async def poll(ctx,*,message):
  polle = discord.Embed(
    title=message
    
  )
  lol = await ctx.send(embed=polle)
  await lol.add_reaction("👍")
  await lol.add_reaction("👎")
  await ctx.respond("Poll started", ephemeral=True)

@client.command(description="Get a prawn picture")
@check(check_if_user_has_premium)
async def pron(ctx):
  pronlist=["https://upload.wikimedia.org/wikipedia/commons/9/98/Penaeus_monodon.jpg","https://www.thefishsociety.co.uk/media/image/e3/1b/b0/prawn-ix.jpg","https://static8.depositphotos.com/1009628/870/i/950/depositphotos_8704465-stock-photo-fresh-prawn.jpg","https://www.thespruceeats.com/thmb/tyRFaxLEOMyqsI__qXeIqTvfyec=/2592x2592/smart/filters:no_upscale()/spotprawns-56b6bfe03df78c0b135b9c3c.jpg"]
  pronpick = random.choice(pronlist)
  await ctx.respond(pronpick)


@client.command(description="Get a random picture!")
@check(check_if_user_has_premium)
async def imagesearch(ctx, image):
  embed = discord.Embed(
    title = 'Image',
    description = 'Your image',
    colour = discord.Colour.purple()
    )
  embed.set_image(url='https://source.unsplash.com/1600x900/?{}'.format(image))            
  embed.set_footer(text=f"{image}")
  await ctx.respond(embed=embed)

@client.command(description="Look up a github repo or user!")
@check(check_if_user_has_premium)
async def github(ctx,owner,repo=None):
  if repo==None:
    await ctx.respond(f"https://github.com/{owner}")
  else:
    await ctx.respond(f"https://github.com/{owner}/{repo}")

@client.command(description="Get a link for a spotify artist!")
@check(check_if_user_has_premium)
async def spotify(ctx,artist):
  await ctx.respond(f"https://open.spotify.com/search/{artist}")

@client.command(description="Get a link to info on a pokemon!")
@check(check_if_user_has_premium)
async def pokemon(ctx,pokemon):
  await ctx.respond(f"https://pokemon.com/us/pokedex/{pokemon}")

@client.command(description="Set a slowmode!")
@commands.has_permissions(manage_channels=True)
@check(check_if_user_has_premium)
async def slowmode(ctx,seconds:int):
  await ctx.channel.edit(slowmode_delay=seconds)
  await ctx.respond(f"Set the slowmode delay in this channel to {seconds} seconds!")

@client.command(description="See how many days ago the bot was created!")
@check(check_if_user_has_premium)
async def createday(ctx):
  your_date = datetime.date(2022, 1, 26)
  today = datetime.date.today()
  delta = (today - your_date).days
  await ctx.respond(f"FetchBot was created {delta} days ago")


@client.command(description="Get information about a shortening")
@check(check_if_user_has_premium)
async def shortening(ctx, *, shortening):
  if shortening.lower()=="btw":
    await ctx.respond("btw means; By the way")
  elif shortening.lower()=="omg":
    await ctx.respond("omg means; Oh my god")
  elif shortening.lower()=="ty":
    await ctx.respond("ty means; Thank you")
  elif shortening.lower()=="thx":
    await ctx.respond("thx means; Thanks")
  else:
    await ctx.respond("I don't have that shortening in my database. You could try with omg, or ty for example :)")

#ECONOMY COMMANDS BELOW ONLY

async def open_account(user):
  users = await get_bank_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["Wallet"] = 0
    users[str(user.id)]["Bank"] = 0

  with open("bank.json", 'w') as f:
    json.dump(users, f)

  return True

async def open_inventory(userinv):
  usersinv = await get_inventory_data()

  if str(userinv.id) in usersinv:
    return False
  else:
    usersinv[str(userinv.id)] = {}
    usersinv[str(userinv.id)]["Inventory"] = 0

  with open("inventory.json", "w") as f:
    json.dump(usersinv, f)
  

async def get_bank_data():
  with open("bank.json", 'r') as f:
    users = json.load(f)
  
  return users

async def get_inventory_data():
  with open("inventory.json", 'r') as f:
    userinv = json.load(f)

  return userinv



async def update_bank(user,change = 0,mode = "Wallet"):
  users = await get_bank_data()
  users[str(user.id)][mode] += change
  with open("bank.json","w") as f :
    json.dump(users,f)
  bal = [users[str(user.id)]    ["Wallet"],users[str(user.id)]["Bank"]]
  return bal

async def setmoney(user,change = 0,mode = "wallet"):
  users = await get_bank_data()
  users[str(user.id)][mode] = change
  with open("bank.json","w") as f :
    json.dump(users,f)
  bal = [users[str(user.id)]  ["Wallet"],users[str(user.id)]["Bank"]]
  return bal

@client.command(description="Set someones balance")
@commands.has_permissions(administrator=True)
async def set(ctx,member:discord.Member,amount:int,mode="Wallet"):
  possible = ["Wallet","Bank"]
  if mode not in possible : 
    await ctx.respond(f":x: Where is {mode} ? Please enter bank or wallet.")
    return
  await open_account(member)
  await setmoney(member,amount,mode)
  await ctx.respond(f":white_check_mark: Set {member.mention}'s {mode} to {amount}")
  return

@client.command(description="See your bank balance!")
async def balance(ctx):
  await open_account(ctx.author)

  user = ctx.author

  users = await get_bank_data()

  wallet_amt = users[str(user.id)]["Wallet"]
  bank_amt = users[str(user.id)]["Bank"]

  em = discord.Embed(title=f"{ctx.author.name}'s balance.", color=discord.Color.teal())
  em.add_field(name="Wallet Balance", value=wallet_amt)
  em.add_field(name="Bank Balance", value=bank_amt)
  await ctx.respond(embed=em)

@client.command(description="See another members' balance")
async def memberbalance(ctx,member:discord.Member):
  await open_account(member)

  user = member

  users = await get_bank_data()

  wallet_amt = users[str(user.id)]["Wallet"]
  bank_amt = users[str(user.id)]["Bank"]

  em = discord.Embed(title=f"{member.name}'s balance.", color=discord.Color.teal())
  em.add_field(name="Wallet Balance", value=wallet_amt)
  em.add_field(name="Bank Balance", value=bank_amt)
  await ctx.respond(embed=em)

@client.command(description="View your inventory")
async def inventory(ctx):
  await open_inventory(ctx.author)

  userinv = ctx.author

  usersinv = await get_inventory_data()

  items = usersinv[str(userinv.id)]["Inventory"]

  if items==1:
    items="Gun"
  elif items==2:
    items="Armour"
  elif items==3:
    items="Mouse"
    

  em = discord.Embed(title=f"{ctx.author.name}s inventory", color=discord.Color.teal())
  em.add_field(name="Inventory", value=items)
  await ctx.respond(embed=em)

@client.command(description="View another members' inventory")
async def memberinventory(ctx,member:discord.Member):
  await open_inventory(member)

  userinv = member

  usersinv = await get_inventory_data()

  items = usersinv[str(userinv.id)]["Inventory"]

  if items==1:
    items="Gun"
  elif items==2:
    items="Armour"
  elif items==3:
    items="Mouse"
    

  em = discord.Embed(title=f"{member.name}s inventory", color=discord.Color.teal())
  em.add_field(name="Inventory", value=items)
  await ctx.respond(embed=em)
  

@client.command(description="Beg for coins!")
@commands.cooldown(1, 300, commands.BucketType.user)
async def beg(ctx):
  await open_account(ctx.author)

  user = ctx.author

  users = await get_bank_data()

  earnings = random.randint(1, 21)

  await ctx.respond(f"Someone gave you {earnings} coins")

  users[str(user.id)]["Wallet"] += earnings

  with open("bank.json", 'w') as f:
    json.dump(users, f)

@client.command(description="Get your daily reward!")
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
  await open_account(ctx.author)

  user = ctx.author

  users = await get_bank_data()

  earnings = random.randint(50, 101)

  await ctx.respond(f"You earned {earnings} from selling some stuff online!")

  users[str(user.id)]["Bank"] += earnings

  with open("bank.json", 'w') as f:
    json.dump(users, f)

@client.command(description="Do a bank robbery!")
@commands.cooldown(1, 3000, commands.BucketType.user)
async def rob(ctx):
  await open_account(ctx.author)

  user = ctx.author

  users = await get_bank_data()

  earnings = random.randint(300, 800)

  wallet_amt = users[str(user.id)]["Wallet"]

  decider = random.randint(0,2)

  if decider == 1:
    await ctx.respond(f"You just robbed the bank and got {earnings}!")

    users[str(user.id)]["Wallet"] += earnings

    with open("bank.json", 'w') as f:
      json.dump(users, f)
  else:
    if wallet_amt > 500:
      await ctx.respond("The police managed to catch you when you robbed the bank :pensive: They also took 500 credits from you")
      users[str(user.id)]["Wallet"] -=500

      with open("bank.json", 'w') as f:
        json.dump(users, f)
    else:
      await ctx.respond(f"The police managed to catch you when you robbed the bank, and they also took {wallet_amt} credits from you! :pensive:")
      users[str(user.id)]["Wallet"] -=wallet_amt

      with open("bank.json", 'w') as f:
        json.dump(users, f)

@client.command(description="Give some of your money to another member!")
async def pay(ctx,amount,member:discord.Member):
  if amount == None : 
    return await ctx.respond(":x: Please enter  a proper amount of money!")
  try :
    int(amount)
  except : 
    return await ctx.respond(":x: Amount can only be a number!")
  await open_account(ctx.author)
  await open_account(member)
  if member == ctx.author :
    await ctx.respond("It's not a good idea to pay yourself")
                
    return
  bal = await update_bank(ctx.author)
  if amount == "all":
    amount = bal[0]
  try :
    amount = int(amount)
  except :
    await ctx.respond("Please enter a valid number")
    return
  if amount>bal[0]:
    await ctx.respond("Please make sure you have enough money in your wallet!")
    return
  if amount<0:
    await ctx.respond("Please enter a number bigger than 1")
                
    return 

  await update_bank(ctx.author,-1*amount,"Wallet")
  await update_bank(member,amount,"Wallet")  

  await ctx.respond(f":white_check_mark: Transaction completed! {amount} has been transfered to {member.name}")
  

@client.command(description="Rob another member!")
@commands.cooldown(1, 1000, commands.BucketType.user)
async def robmember(ctx,member:discord.Member):
  await open_account(ctx.author)
  await open_account(member)
  user = ctx.author

  mem = member

  users = await get_bank_data()

  earnings = random.randint(100, 500)

  wallet_aamt = users[str(user.id)]["Wallet"]

  decider = random.randint(0,2)

  wallet_amt = users[str(mem.id)]["Wallet"]

  if wallet_amt < earnings:
    if wallet_amt < 0:
      await ctx.respond("It's not worth it :pensive:")
      return
    elif wallet_amt == 0:
      await ctx.respond("It's not worth it :pensive:")
      return
    else:
      earnings = wallet_amt

  
  if decider == 1:
    await ctx.respond(f"You just robbed {member} and got {earnings} credits!")

    users[str(user.id)]["Wallet"] +=earnings
    users[str(mem.id)]["Wallet"] -=earnings

    with open("bank.json", 'w') as f:
      json.dump(users, f)
  else:
    responselist=[f"{mem} knew how to defend themselfs and took 100 credits from you instead!", f"{mem} killed you and took 100 credits from you!", "A dog killed you and ate 100 credits!"]
    choice = random.choice(responselist)
    await ctx.respond(choice)
    if wallet_aamt > 100:
      users[str(user.id)]["Wallet"] -= 100

      with open("bank.json", "w") as f:
        json.dump(users, f)
    else:
      ammountt = wallet_aamt
      users[str(user.id)]["Wallet"] -=ammountt

      with open("bank.json", 'w') as f:
        json.dump(users, f)
      
    

@client.command(description="Transfer money from your wallet to the bank")
async def deposit(ctx,amount):
  if amount == None : 
    return await ctx.respond(":x: Please enter  a proper amount of money!")
  try :
    int(amount)
  except : 
    return await ctx.respond(":x: Amount can only be a number!")
  await open_account(ctx.author)
          
  bal = await update_bank(ctx.author)
  amount = int(amount)
  if amount>bal[0]:
    await ctx.respond(":x: You don't have the enough amount !")
                  
    return
  if amount<0:
    await ctx.respond(":x: Please enter a number bigger than 1.")
                  
    return 

  await update_bank(ctx.author,-1*amount)
  await update_bank(ctx.author,amount,"Bank")  

  await ctx.respond(f":moneybag: You just deposited {amount} dollars.")

@client.command(description="Transfer money from your wallet to the bank")
async def withdraw(ctx,amount):
  if amount == None : 
    return await ctx.respond(":x: Please enter  a proper amount of money!")
  try :
    int(amount)
  except : 
    return await ctx.respond(":x: Amount can only be a number!")
  await open_account(ctx.author)
  bal = await update_bank(ctx.author)
  amount = int(amount)
  if amount>bal[1]:
    await ctx.respond(":x: You don't have the enough amount !")
                
    return
  if amount<0:
    await ctx.respond(":x: Please enter a number bigger than 1.")
                    
    return 
        
  await update_bank(ctx.author,amount)
  await update_bank(ctx.author,-1*amount,"Bank")  

  await ctx.respond(f":moneybag: You withdrew {amount} dollars.")

@client.command(description="Buy something")
async def buy(ctx,item):
  await open_account(ctx.author)
  await open_inventory(ctx.author)

  user=ctx.author

  userinv=ctx.author

  cost=2500
  
  users=await get_bank_data()

  usersinv=await get_inventory_data()

  wallet_amt = users[str(user.id)]["Wallet"]
  bank_amt = users[str(user.id)]["Bank"]

  if wallet_amt < cost:
    if bank_amt > cost:
      await ctx.respond(f"You don't have enough money in your wallet! Try to buy something online instead with your online wallet! This item costs {cost} credits.")
      return
    else:
      await ctx.respond(f"Buying something costs {cost} currently! You have less than that!")
      return
  
  if item.lower()=="gun":
    itemcode=1
    
    await ctx.respond(f"You just bought {item}! It has been stored in your inventory.")

    users[str(user.id)]["Wallet"] -= cost

    with open("bank.json", "w") as f:
      json.dump(users, f)

    usersinv[str(userinv.id)]["Inventory"] = itemcode

    with open("inventory.json", "w") as f:
      json.dump(usersinv, f)
  elif item.lower()=="armour":
    itemcode=2

    await ctx.respond(f"You just bought {item}! It has been stored in your inventory.")

    users[str(user.id)]["Wallet"] -= cost

    with open("bank.json", "w") as f:
      json.dump(users, f)

    usersinv[str(userinv.id)]["Inventory"] = itemcode

    with open("inventory.json", "w") as f:
      json.dump(usersinv, f)

  elif item.lower()=="mouse":
    itemcode=3

    await ctx.respond(f"You just bought {item}! It has been stored in your inventory.")

    users[str(user.id)]["Wallet"] -= cost

    with open("bank.json", "w") as f:
      json.dump(users, f)

    usersinv[str(userinv.id)]["Inventory"] = itemcode

    with open("inventory.json", "w") as f:
      json.dump(usersinv, f)
  
  else:
    await ctx.respond("This is not a valid item! Use /shop to get a list of purchasable items!")


@client.command(description="View the shop")
async def shop(ctx):
  embed=discord.Embed(
    title="Shop"
  )
  embed.add_field(name="Buy things with money!", value="Gun\nArmour\nMouse")
  await ctx.respond(embed=embed)

@client.command(description="View the leaderboard")
async def leaderboard(ctx):
  limit = 3
  try :
            
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
      name = int(user)
      total_amount = users[user]["Wallet"] + users[user]["Bank"]
      leader_board[total_amount] = name
      total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {limit} Richest People" , description = "This is decided on the basis of the ammount money in the bank and wallet",color = random.randrange(0, 0xffffff))
    index = 1
    for amt in total:
      id_ = leader_board[amt]
      member = client.get_user(id_)
      name = member.name
      em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
      if index == limit:
        break
      else:
        index += 1
        em.set_footer(text =f"Requested By {ctx.author}")
        await ctx.respond(embed = em)
  except AttributeError:
    await ctx.respond(":x: There are not that many accounts stored in my database.")

def setup(client):
  client.add_cog(greetings(bot))


client.load_extension('cogs.moderation')
client.run(TOKEN)
