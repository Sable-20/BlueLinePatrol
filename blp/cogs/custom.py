import discord
from discord.ext import commands

class custom(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(aliases=['youtube'])
    async def yt(self, ctx):
        embed = discord.Embed(title="https://www.youtube.com/bluelinepatrol")
        await ctx.send(embed=embed)

    @commands.command(aliases=['insta'])
    async def instagram(self, ctx):
        embed = discord.Embed(title="https://www.instagram.com/blue_linepatrol/")
        await ctx.send(embed=embed)

    @commands.command()
    async def twitter(self, ctx):
        embed = discord.Embed(title="https://twitter.com/PatrolBlue")
        await ctx.send(embed=embed)

    @commands.command()
    async def twitch(self, ctx):
        embed = discord.Embed(title="https://www.twitch.tv/awayback_") 
        await ctx.send(embed=embed)   

    @commands.command()
    async def spotify(self, ctx):
        embed = discord.Embed(title="https://open.spotify.com/playlist/0fxALJND5xC3L9CbZYBi8f?si=RjhkYlhESQiGLItGNngmdg")
        await ctx.send(embed=embed)

    @commands.command(aliases=["merch"])
    async def merchandise(self, ctx):
        embed = discord.Embed(title="https://teespring.com/de/stores/bluelinepatrols-merch")
        await ctx.send(embed=embed)

    @commands.command(aliases=['web'])
    async def website(self, ctx):
        embed = discord.Embed(title="Coming soon...")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(custom(bot))
    print("\ncustom cog loaded\n---------\n")