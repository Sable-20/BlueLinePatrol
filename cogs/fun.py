import discord
from discord.ext import commands
import random
import asyncio
import math
from PIL import Image
from io import BytesIO

class fun(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        self.last = {}

    # for the funny haha
    @commands.command(aliases=['isrp'])
    async def rp(self, ctx):
        embed = discord.Embed()
        embed.description = "Blue Line Patrol is ***not*** an RP server"
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot or len(message.content) == 0:
            return #checks if there was nothing in the message deleted ( in case discord bugged out )
        
        self.last[message.channel] = [str(message.author), message.author.avatar_url_as(static_format="png0"), message.content]
        return #just adds the message to a list and save the author avatar
    
    @commands.command()
    async def snipe(self, ctx):
        if ctx.channel not in self.last: #if nothing is in the list
            return await ctx.send(embed=discord.Embed(
            description="There is nothing to snipe.",
            color=discord.Color.red() #R E D
            ))
        #Send the embed
        await ctx.send(embed=discord.Embed(
        title="Sniped Message",
        description=self.last[ctx.channel][-1],
        color=discord.Color.green() # G R E E N
        )
        .set_author(name=self.last[ctx.channel][0], icon_url=self.last[ctx.channel][1])) # grabbing the message and the author
        #Remove it from the dictionary
        del self.last[ctx.channel]
        return

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        # 8 ball shitty responses
        responses = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes – definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy, try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ]

        randchoice = random.choice(responses)
        # just initializing the embde and sending it
        em = discord.Embed(title="8ball magik")
        em.add_field(name="Question: ", value=f"{question}", inline=True)
        em.add_field(name="Answer: ", value=f"{randchoice}", inline=True)
        await ctx.send(embed=em)

    #coinflip just chooses heads of tails
    @commands.command()
    async def coinflip(self, ctx):
        choices = [
            "heads",
            "tails"
        ]

        embed = discord.Embed(title="And the answer is....", description=f"{random.choice(choices)}")#fancy shit
        await ctx.send(embed=embed) # sends embed   

    #dunno why i included this but its fun
    @commands.command()
    async def gayrate(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.message.author
        # randomly chooses number from 20 to 100
        percent = math.floor(random.random()*101 + 20)

        #saying how G A Y one is
        embed = discord.Embed(title=f"{member} is **{percent}%** gay!")
        await ctx.send(embed=embed)

    #horny jail may have to remove
    @commands.command(aliases=['hj'])
    async def hornyjail(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("You cant send yourself to horny jail")

        else:
            embed = discord.Embed(title=f"go to horny jail {member}")
            embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.tenor.com%2Fimages%2F8171c146496d29c960e05759926482ae%2Ftenor.gif&f=1&nofb=1")
            embed.set_footer(text="Powered by the horny cops")
            await ctx.send(embed=embed)

    #b o n k
    @commands.command(aliases=['bnk'])
    async def bonk(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("You cant bonk yourself")
        else:
            embed = discord.Embed(title=f"{ctx.author} has bonked {member}")
            embed.set_image(url="https://images-cdn.9gag.com/photo/aNzY160_700b.jpg")
            embed.set_footer(text=f"This was powered by the server monkeys")
            await ctx.send(embed=embed)

    #thanks someone may have to work on optimizing it like yag
    @commands.command(aliases=["thank"])
    async def thanks(self, ctx, member: discord.Member=None):
        if not member:
            await ctx.send('You cant thank yourself -.-')

        else:
            embed = discord.Embed(title=f"{ctx.message.author} thanked {member}!❤")
            await ctx.send(embed = embed)

    #WIP
    @commands.command()
    async def wanted(self, ctx, member: discord.Member=None): 
        if not member:
            member = ctx.message.author
            
        wanted = Image.open("images/wanted.jpg")

        asset = member.author.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((503, 486))

        wanted.paste(pfp, (199, 406))

        wanted.save("profile.jpg")

        await ctx.send(file = discord.File("profile.jpg"))

    #owner only
    @commands.command(aliases=["fuck", "fuck this", "fuckthisbot"])
    @commands.is_owner()
    async def fuckthis(self, ctx):
        embed = discord.Embed(title="fuck this fucking bot")
        embed.set_image(url="https://tenor.com/view/fuck-this-shit-gif-14035982")
        embed.set_footer(text="powered by the fuckery that is code")

        await ctx.send(embed=embed) 

    #not including this in the help command
    #######################################
    # DO NOT INCLUDE IN HELP COMMAND
    #######################################
    @commands.command()
    async def spank(self, ctx, member: discord.Member):
        if not member:
            ctx.send("Cant spank yourself silly")
        
        embed = discord.Embed(title=f"Get spanked {member}")
        embed.set_image(url="https://gifimage.net/wp-content/uploads/2017/09/anime-spanking-gif.gif")
        ctx.send(embed=embed)

    # b o o m e r
    @commands.command(aliases=["boomer"])
    async def okboomer(self, ctx):
        boomers = [
            "https://www.barnorama.com/wp-content/uploads/2019/06/smile_to_hide_your_inner_pain-2.jpg",
            "https://www.incimages.com/uploaded_files/image/970x450/getty_665831230_368631.jpg",
            "https://wordbrothel.com/wp-content/uploads/2018/01/BabyBoomers.jpg",
            "https://tse4.mm.bing.net/th?id=OIP.Vj8-jPkIs8PIsKhENKUDxwHaEt&pid=Api&P=0&w=278&h=178",
            "https://melmagazine.com/wp-content/uploads/2018/10/01OxOnVEFqRP5jBKC.html-charsetutf-8",
            "https://ruinmyweek.com/wp-content/uploads/2019/11/tk-memes-making-fun-of-boomers-1.png",
            "https://cdn-images-1.medium.com/max/1600/0*LgMxUC_x4QoC3lVU",
            "https://thefunnybeaver.com/wp-content/uploads/2020/08/boom.jpg",
            "https://filmdaily.co/wp-content/uploads/2020/06/Ok-boomer-Lede.jpg",
            "https://i.ytimg.com/vi/skrtipuN7wo/maxresdefault.jpg",
            "https://video-images.vice.com/articles/5c86b6ec5b9f2f0008c3671e/lede/1552333333777-deepfried_1552333269726.png?crop=1xw:0.99375xh;center,center&resize=1200:*",
            "https://screenfish.net/wp-content/uploads/2019/11/ok-boomer-1024x722.jpg",
            "https://i.redd.it/ru40jmsfxge41.jpg",
            "https://3h7pwd17k2h42n17eg2j7vdq-wpengine.netdna-ssl.com/wp-content/uploads/2019/11/jarvis_boomer-1.jpg",
            "https://davidyat.es/content/images/2018/09/boomer0.png"
        ]

        boomerjoke = random.choice(boomers)

        embed = discord.Embed(title="OK Boomer")
        embed.set_image(url=boomerjoke)
        embed.set_footer(text="ok BOOMER")

        await ctx.send(embed=embed)

    #mhmmmmmm
    #mhmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
    # l o v e y d o v e y
    @commands.command(aliases=["lovers", "love", "ratemylove"])
    async def loverate(self, ctx, member: discord.Member):
        if not member:
            await ctx.send("Im afraid I cant rate the love of yourself")

        else:
            love_percent = round(random.randint(0,100))
            embed = discord.Embed(title="Love Rate",
                                color = discord.Color.dark_magenta())
            embed.add_field(name=f"And the love rating between {ctx.message.author} and {member} is...", value=f"***{love_percent}%***")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))
    print("fun cog loaded\n------\n")