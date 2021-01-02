import discord
from discord.ext import commands
import random
import math
import sys
import traceback
import json
# import mysql.connector
# import pymongo
# import dns


filtered_words = ["cock",
                  "hore",
                  "motherfucker",
                  "fucker",
                  "asshole",
                  "dick",
                  "dickhead",
                  "mother-fucker",
                  "fcker",
                  "cumquat",
                  "shithead",
                  "queer",#maybe revists
                  "cocksucker",
                  "cunt",
                  "fag",
                  "faggot",
                  "kyke", #never hear of this
                  "dyke",
                  "nigger",
                  "niger",
                  "n1gg3r",
                  "n1gg@",
                  "nigg@",
                  "nigg3r"]

filtup = filtered_words.upper()




bot = commands.Bot(command_prefix='.', case_insensitive=True, owner_ids=[451484425591586817, 561291092809482240])
bot.remove_command('help')

initial_extensions = ['cogs.moderation',
                      'cogs.loadup',
                      'cogs.manage',
                      'cogs.utility',
                      'cogs.fun',
                      'cogs.custom']

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load {extension}', file=sys.stderr)
            traceback.print_exc()   


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}\n\nWith ID: {bot.user.id}")

@bot.command(aliases=["logoff"])
@commands.is_owner()
async def logout(ctx):
    await ctx.send(f"{ctx.message.author} I'm logging off now")
    await bot.logout()

@logout.error
async def logout_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("you dont have permission to use this command")
    else:
        pass

###################################################################
#LEVELING
###################################################################

@bot.listen('on_message')
async def on_message(message):
    if message.author.bot:
        return

    
    for word in filtered_words:
        if word in message.content:
            await message.delete()
            embed = discord.Embed()
            embed.description = f"{message.author.id} please refrain from using that word. ~BLP staff"
            await message.channel.send(embed=embed)
    
    for word in filtup:
        if word in message.content:
            await message.delete()
            embed = discord.Embed()
            embed.description = f"{message.author.id} please refrain from using that word. ~BLP staff"
            await message.channel.send(embed=embed)


    # cursor = mydb.cursor()


    # cursor.execute("SELECT user_xp, user_level FROM users WHERE client_id = " + str(message.author.id)) 
    # result = cursor.fetchall()
    # print(result)
    # if(len(result) == 0):
    #     print("User is not in the database.... creating slot")
    #     cursor.execute("INSERT INTO users VALUE(" + str(message.author.id) + "," + str(xp) + ", 1)")
    #     mydb.commit()
    #     embed = discord.Embed()
    #     embed.set_author(name="Catalyst")
    #     embed.description = f"You just leveled up to level 1"
    #     await message.channel.send(embed=embed)
    # else:
    #     newXP = result[0][0] + xp
    #     currentLevel = result[0][1]
    #     xp_start = result[0][1]
    #     xp_end = result[0][0] ** (1.5 / 8)

    #     if xp_end > xp_start:
    #         nextLevel = currentLevel+1
    #         embed = discord.Embed()
    #         embed.set_author(name="Copper")
    #         embed.description = f"{message.author} has leveled up to {nextLevel}"
    #         await message.channel.send(embed=embed)
    #         cursor.execute(f"UPDATE users SET user_xp = '{newXP}', user_level = '{nextLevel}' WHERE client_id = '{message.author.id}'")
    #         mydb.commit()
    #         print("Database updated...")
    #     else:
    #         cursor.execute(f"UPDATE users SET user_xp = '{newXP}', user_level = '{currentLevel}' WHERE client_id = '{message.author.id}'")
    #         mydb.commit()
    #         print("Database updated...")



###########################################################
#    H E L P C O M M A N D
###########################################################

@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="Help", description="Use .help [category] to see more info on the commands in that category", color=ctx.author.color)
    embed.add_field(name="Moderation", value="Purge, Kick, Ban, Softban, Unban, Mute, Unmute, Slowmode, Lockdown, Nuke")
    embed.add_field(name="Utility", value="Invite, Whois, Serverinfo, Ping, Report")
    embed.add_field(name="Fun", value="8ball, Coinflip, Gayrate, Bonk, Thanks, Okboomer, Loverate")
    embed.add_field(name="Custom Commands", value="yt, insta, twitter, twitch, spotify, merch")
    embed.add_field(name="How to get help?", value=".help [category]")
    await ctx.send(embed=embed)

@help.command()
async def moderation(ctx):
    embed = discord.Embed(title="Moderation")
    embed.add_field(name="Purge", value="Purges the specified amoutn of messages... default is two\n.purge 2")
    embed.add_field(name="Kick", value="Kicks specified member\n.kick @misaka")
    embed.add_field(name="Ban", value="Bans the specified member\n.ban @misaka")
    embed.add_field(name="Softban", value="Bans and immediately unbans member to clear their messages\n.softban @misaka")
    embed.add_field(name="Unban", value="Unbans a member, their full username and discriminator must be mentioned\n.unban misaka#XXXX")
    embed.add_field(name="Hardute", value="Mutes the specified member... if the role does not exist the bot will create one\n.hmute @misaka")
    embed.add_field(name="Unhardmute", value="Unmutes the specified member\n.unhmute @misaka")
    embed.add_field(name="Slowmode", value="Sets the slow mode of a channel to the specified amount of ***seconds***\n.slowmode 5")
    embed.add_field(name="Lockdown", value="***WIP***\nComing Soon....")
    embed.add_field(name="Nuke", value="nukes the channel by deleting as many messages as possible\n.nuke")
    await ctx.send(embed=embed)

@help.command()
async def utility(ctx):
    embed = discord.Embed(title="Utility")
    embed.add_field(name="Invite", value="Creates a permanent invite link to the current channel\n.invite")
    embed.add_field(name="Whois", value="Gets basic user info on the specified member\n.userinfo @misaka")
    embed.add_field(name="Serverinfo", value="Displays info about the server\n.serverinfo")
    embed.add_field(name="Ping", value="Pong")
    embed.add_field(name="Report", value="***WIP***\nReports a mentioned member for the reason you type after\n.report @misaka being a bitch")
    await ctx.send(embed=embed)

@help.command()
async def fun(ctx):
    # 8ball, Coinflip, Gayrate, Bonk, Thanks, Okboomer, Loverate
    embed = discord.Embed(title="Fun")
    embed.add_field(name="8ball", value="Gives you an answer for the question you asked\n.8ball is misaka gay?")
    embed.add_field(name="Coinflip", value="Flips a coin, heads or tails?")
    embed.add_field(name="Gayrate", value="Just how gay :thinking:")
    embed.add_field(name="Bonk", value="Bonk someone you mentioned\n.bonk @JonE")
    embed.add_field(name="Thanks", value="Thanks a mentioned member")
    embed.add_field(name="okboomer", value="***O K B O O M E R***")
    embed.add_field(name="Loverate", value="rate the love in the air")
    embed.add_field(name="Snipe", value="***WIP***\n.snipe")                
    await ctx.send(embed=embed)

@help.command()
async def custom(ctx):
    #yt, insta, twitter, twitch, sportify, merch
    embed = discord.Embed(title="Custom Commands")
    embed.add_field(name="yt", value="Send a link the Blue Line Patrol's youtube channel")
    embed.add_field(name="insta", value="Send a link to Blue Line Patrol's instagram")
    embed.add_field(name="twitter", value="Send a link to Blue Line Patrol's twitter")
    embed.add_field(name="twitch", value="Send a link to Blue Line Patrol's twitch channel")
    embed.add_field(name="spotify", value="Send a link the Blue Line Patrol's spotify")
    embed.add_field(name="merch", value="Send a link to Blue Line Patrol's M E R C H")
    await ctx.send(embed=embed)

bot.run("NzkwOTQ1ODM1MTg0NTUzOTg0.X-H_tg.O15gUqUoTNLWVuoJiR8oo4t7CXo")