import discord
from discord.ext import commands
import math

class utility(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def invite(self, ctx):
        link = "https://discord.gg/pXWwUhed3h"
        embed = discord.Embed()
        embed.description = f"Your invite is\n\n{link}"
        await ctx.send(embed=embed)

    @commands.command(aliases=['latency', 'pong'])
    async def ping(self, ctx):
        await ctx.send(f"Pong! My latency is {round(self.bot.latency*1000)} ms")

    @commands.command(aliases=['userinfo'])
    async def whois(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.message.author
        roles = [role for role in member.roles]
        embed = discord.Embed(color=discord.Color.purple(),
                              timestamp=ctx.message.created_at,
                              title=f"User info - {member}")
        
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")

        embed.add_field(name="ID: ", value=member.id, inline=False)
        embed.add_field(name="Display Name: ", value=member.display_name, inline=False)

        embed.add_field(name="Created Account On: ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined Server On: ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)

        embed.add_field(name="Roles: ", value="".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="Highest Role: ", value=member.top_role.mention, inline=False)
        print(member.top_role.mention)
        await ctx.send(embed=embed)

    @commands.command(aliases=['si'])
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            color=discord.Color(0xffff),
            title=f"{ctx.guild.name}"
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="Region: ", value=f"`{ctx.guild.region}`")
        embed.add_field(name="Member Count: ", value=f"{ctx.guild.member_count}")
        embed.add_field(name="Owner: ", value=f"{ctx.guild.owner}")
        embed.add_field(name="Verification Level: ", value=f"{ctx.guild.verification_level}")
        embed.add_field(name="Content Filter: ", value=f"{ctx.guild.explicit_content_filter}")
        embed.add_field(name="Number of Boosts: ", value=f"{ctx.guild.premium_subscription_count}")
        embed.add_field(name="Premium Tier: ", value=f"{ctx.guild.premium_tier}")
        embed.set_footer(icon_url=f"{ctx.guild.icon_url}", text=f"Guild ID: {ctx.guild.id}")

        await ctx.send(embed=embed)

    @commands.command()
    async def report(self, ctx, member: discord.Member, *, reason):
        rchannel = ctx.get_channel(738667684899717220)

        embed = discord.Embed(title=f"New report")
        embed.add_field(name="Reporter: ", value=f"{ctx.author.mention}")
        embed.add_field(name="Reportee: ", value=f"{member.mention}")
        embed.add_field(name="Reason: ", value=f"{reason}")
        await rchannel.send(embed=embed)

def setup(bot):
    bot.add_cog(utility(bot))
    print("Utility cog loaded\n----------\n")