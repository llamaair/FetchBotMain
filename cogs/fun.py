import discord
from discord.ext import commands
import asyncio
import random

class fun(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command() # we can also add application commands
    async def goodbye(self, ctx):
        await ctx.respond("Bye")

    @discord.slash_command(description="Get a cute cat picture")
    async def cat(self, ctx):
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


    @discord.slash_command(description="Get a cute dog picture")
    async def dog(self, ctx):
        await ctx.respond(
        "https://i.natgeofe.com/n/3faa2b6a-f351-4995-8fff-36d145116882/domestic-dog_16x9.jpg"
    )


    @discord.slash_command(description="Get a picture of a fat cat!")
    async def fatcat(self, ctx):
        await ctx.respond(
        "https://live.staticflickr.com/3652/3513292420_6becf54bbf.jpg")


    @discord.slash_command(description="Get a picture of a fat dog!")
    async def fatdog(self, ctx):
        fatdoglist = [
        "https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Fmobile%2F000%2F029%2F671%2Fwide_dog_cover2_.jpg",
        "https://s.abcnews.com/images/Entertainment/HT_vincent4_dog_ml_160413_16x9_608.jpg"
    ]
        fatdogchoise = random.choice(fatdoglist)
        await ctx.respond(fatdogchoise)

    @discord.slash_command(description="Print a random fact")
    async def fact(self, ctx):
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
        
    @discord.slash_command(description="Get a random challenge!")
    async def challenge(self, ctx):
        challengelist=["Eat a hamburger in 20 seconds", "Say yeet in your most southern accent", "Don't speak today", "Stop watching TV", "Eat slower today", "Do 15 sit-ups", "Learn to draw a face", "Don't drink soda today", "Do something you are scared of", "Abuse FetchBot"]
        challenge = random.choice(challengelist)
        await ctx.respond(challenge)



    @discord.slash_command(description="Abuse someone!")
    async def abuse(self, ctx, user:discord.Member):
        if user.bot:
            randlist=[f"kills {ctx.author.mention}", f"kicks {ctx.author.mention} out of the server", f"eats {ctx.author.mention}", f"abuses {ctx.author.mention}", f"eyes {ctx.author.mention} slowly"]
            randresponse=random.choice(randlist)
            await ctx.respond(f"*{randresponse}*")
        else:
            await ctx.respond(f"*{ctx.author} abuses {user}*")

    @discord.slash_command(description="How stupid are you?")
    async def stupid(self, ctx):
        stupidlist=['100%', '39%', '0%', '50%', '70%', '20%', '95%', '13%']
        stupidity= random.choice(stupidlist)
        await ctx.respond(f"You are {stupidity} stupid")

    @discord.slash_command(description="How smart are you?")
    async def smart(self, ctx):
        smartlist=["0%", "100%", "50%", "20%", "67%"]
        smart = random.choice(smartlist)
        await ctx.respond(f"You are {smart} smart!")
    
    @discord.slash_command(description="Ask me a question!")
    async def ask(self, ctx, *, question):
        responselist=['Yes', 'No', 'Maybe', 'Sure!', 'Of course!', 'Why not', 'I am tired! Ask me later instead.', 'I have no idea', 'Stupid humans...']
        response = random.choice(responselist)
        await ctx.respond(response)

    @discord.slash_command(description="Get a anime picture")
    async def anime(self, ctx):
        animelist = [
        "https://cdn.vox-cdn.com/thumbor/I7I0t87KZ-vf_GSWrH118jwl6d0=/1400x0/filters:no_upscale()/cdn.vox-cdn.com/uploads/chorus_asset/file/23437452/The_Spy_x_Family_Anime_Succeeds_Because_of_Its_Characters_.jpg",
        "https://androspel.com/wp-content/uploads/2022/03/anime-dimensions-tier-list.jpg",
        "https://www.gamespot.com/a/uploads/screen_kubrick/1732/17320263/4019145-anime-dek-image.jpg"
    ]
        animechoise = random.choice(animelist)
        await ctx.respond(animechoise)


    @discord.slash_command(description="Get a manga picture")
    async def manga(self, ctx):
        mangalist = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Figure_in_Manga_style_pattern.png/190px-Figure_in_Manga_style_pattern.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Manga.png/220px-Manga.png",
        "https://en.canson.com/sites/default/files/styles/large/public/medias-images/manga-007.jpg?itok=NxaBiaif"
    ]
        mangachoice = random.choice(mangalist)
        await ctx.respond(mangachoice)

    @discord.slash_command(aliases=['fu'], description="Predict your future")
    async def future(self, ctx):
        futurelist = [
        'You will become poor and homeless',
        'You are going to become rich, and develop a genious tool for Pc;s',
        'You are going to have a decent job that pays a decent ammount of money',
        'You are going to live untill you get 150 years!'
        ]
        future = random.choice(futurelist)
        await ctx.respond(future)



def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(fun(bot)) # add the cog to the bot