import discord
from discord.ext import commands
from datetime import timedelta
from discord.ext.commands import BucketType, cooldown
import asyncio

##################################################
#     T O D O L I S T
##################################################
#    1.) i have to clean up my unban command as its not ideal and relies and being able to get someones display name
#        which they could have changed
#    2.) inspect the nuke command to make sure it works


class moderation(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    #purge
    @commands.command(aliases=["clear"])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=2):
        if amount > 200: #maxes out at 200 messages for lag saving purposes
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "You cannot clear this many messages"
            await ctx.send(embed=embed)
        await ctx.channel.purge(limit=amount)
    
    #kick
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason was provided"): #makes local variables
        if ctx.author.top_role < member.top_role: #checks for higher role
            #dont ask why you can compare a string like its a number
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "You cannot kick someone with a higher role than you"
            await ctx.send(embed=embed)
            return
        elif ctx.author.top_role == member.top_role: #checking if the roles equal eachother
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "You cannot kick someone with the same role as you"
            await ctx.send(embed=embed)
            return
        else: #any other situation
            if member == None:
                embed = discord.Embed()
                embed.set_author(name="BLP")
                embed.description = "Please mention someone to kick"
                await ctx.send(embed=embed)
                return
            try: #attempts to dm them
                await member.send(f"You have been kicked from the guild.\n**REASON: **{reason}")
            except: #in case they have dms disabled
                pass
            await member.kick(reason=reason)
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "Successfully kicked **{}**.".format(member) #sucess message
            await ctx.send(embed=embed)

    #ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason was provided"): #local variables otherwise known as 
        #parameters will be reffered to a variables from now on
        if ctx.author.top_role < member.top_role: #fuckery with checking roles
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "You cannot ban someone with a higher role than you"
            await ctx.send(embed=embed)
            return
        elif ctx.author.top_role == member.top_role: # more role checking
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "You cannot ban someone with the same role as you"
            await ctx.send(embed=embed)
            return
        else:
            if member == None: #bleh
                embed = discord.Embed()
                embed.set_author(name="BLP")
                embed.description = "Please mention someone to ban"
                await ctx.send(embed=embed)
                return
            try:
                await member.send(f"Dear {member}. :wave:\n You have been banned from the BlueLinePatrol Community Server for: {reason}\nYou can no longer rejoin unless you get unbanned. If you want to know how you can get unbanned, read the unban part below. \n\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\nIf you feel like your ban was not right, then fill out this form:\nhttps://forms.gle/iBNsFv3w4eVgB6zi6 \nIf you would like to fill out a ban appeal to be unbanned, please fill out this form: \nhttps://forms.gle/ayaDwW2ZEvdUSxrH7 \n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ \nThank you for understanding. \nYour BLP Staff. \n")
            except:
                pass
            await member.ban(reason=reason)
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "Successfully banned **{}**.".format(member)
            await ctx.send(embed=embed)

    #softban
    @commands.command(aliases=["sb"]) #softabn bans and unbans to clear messages
    @commands.has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason="No reason was provided"): #local variables
        if ctx.author.top_role < member.top_role: #fuckery with roles 
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "You cannot ban someone with a higher role than you"
            await ctx.send(embed=embed)
            return
        elif ctx.author.top_role == member.top_role:
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "You cannot ban someone with the same role as you"
            await ctx.send(embed=embed)
            return
        else:
            if member == None:
                embed = discord.Embed()
                embed.set_author(name="BLP")
                embed.description = "Please mention someone to ban"
                await ctx.send(embed=embed)
                return
            try:
                await member.send(f"You have been soft banned from the guild.\n**REASON: **{reason}")
            except:
                pass
            await member.ban(reason=reason)
            await ctx.guild.unban(member)
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "Successfully soft banned **{}**.".format(member)
            await ctx.send(embed=embed)

    #unban
    #unban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member=None, *, reason="Not provided"):
        if member==None:
            await ctx.send("Who would you like to unban?\n Provide a user next time")
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')

        for banned_entry in banned_users:
            user = banned_entry.user

            if (user.name, user.discrminator) == (member_name, member_disc):
                await ctx.guild.unban(user)
                await ctx.send(member_name + f" was unbanned | {reason}")
                return
        await ctx.send(member + ' not found')   

    #mute
    #mutes a person
    @commands.command(aliases=['hmute'])
    @commands.has_permissions(manage_messages=True)
    async def hardmute(self, ctx, member: discord.Member,*,reason=None):#initializing local variables
        if member == None:#if theyre not mentioned
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "Please mention a member"
            await ctx.send(embed=embed)
            return
        role = discord.utils.get(ctx.guild.roles, name="HardMuted")
        if role not in ctx.guild.roles: #if the role doesnt exist the bot creates one wiht default overwrites
            perms = discord.Permissions(add_reactions=False, send_messages=False, connect=False)
            await ctx.guild.create_role(name="HardMuted", permissions=perms)
            await member.add_roles(role)
            for x in member.roles:
                if x == ctx.guild.default_role:
                    pass
                else:
                    y = discord.utils.get(ctx.guild.roles, name=x.name)
                    await member.remove_roles(y)
            embed = discord.Embed(title=f"{member} has been hard muted")
            await ctx.send(embed=embed)
        else: #if its already made and the bot can access it
            for x in member.roles:
                if x == ctx.guild.default_role:
                    pass
                else:
                    y = discord.utils.get(ctx.guild.roles, name=x.name)
                    await member.remove_roles(y)
            await member.add_roles(role)
            embed = discord.Embed(title=f"{member} has been hard muted")
            await ctx.send(embed=embed)
    
    #unmute
    #self explanatory but it unmutes a person
    @commands.command(aliases=['unhardmute'])
    @commands.has_permissions(manage_roles=True)
    async def unhmute(self, ctx, member: discord.Member=None):
        if member == None: #incase they dont mention a user
            #NOTE: THEY MUST BE MENTIONED 
            #EXAMPLE: @misaka#xxxx
            await ctx.send("Please specify a user!")
            return
        role = discord.utils.get(ctx.guild.roles, name="HardMuted")#find the role 'Muted'
        try:
            await member.remove_roles(role)
            await ctx.send(f"{member} sucessfully un-hard-muted") #removes it
        except Exception:
            await ctx.send("That user isnt hard muted") #incase they arent muted

    #slowmode
    #this should set a slow mode with a maximum of 6 hours
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 60, BucketType.user)
    async def slowmode(self, ctx, time : int=0):
        if time < 0: #checking if its less than 0 seconds
            await ctx.send("Please enter a valid number!")
            return
        try: #incase they accidentally enter a number
            if time > 21600: #checks for over 6 hours 
                await ctx.send("Number is too large, you cannot have a slowmode delay of more than 6 hours")
            else: #as long as it meets all criteria it comes to this and sets the slowmode
                await ctx.channel.edit(slowmode_delay=time)
                await ctx.send(f"The channel {ctx.channel.name} now has a slowmode of {time} seconds")
        except Exception:
            await ctx.send("Not a number!")

    #lockdown
    #in theory this locks down a channel so people with @everyone perms cannot see, 
    # so long as this works as intended only those with admin permission will be able to
    #  speak in the channel
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 5, BucketType.user) #cool down so admins use sparingly
    async def lockdown(self, ctx, channel: discord.channel=None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(send_message=False)
            } #checks if the @everyone role is in overwrites(usually not)
            await channel.edit(overwrites=overwrites)
            await ctx.send(f"**The channel `{ctx.channel.name}` has been locked down**`") #locks it down
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            #this overrides the channel perms
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send("**The channel `{}` has successfully been locked!**".format(ctx.channel.name))
        else:
            #for any other unforseen situation
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send('**The channel `{}` has now been unlocked!**'.format(ctx.channel.name))
    
    ##################################################################
    #WIP
    ##################################################################
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def nuke(self, ctx):
        limit = 99999999999999999
        await ctx.channel.purge(limit=limit)
        embed = discord.Embed(title="Kaboom?")
        embed.set_image(url="http://images5.fanpop.com/image/photos/24800000/Kaboom-rico-the-penguin-24826931-1024-768.jpg")
        embed.set_footer(text="Yes Rico, kaboom")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member,*,reason=None):#initializing local variables
        if member == None:#if theyre not mentioned
            embed = discord.Embed()
            embed.set_author(name="BLP")
            embed.description = "Please mention a member"
            await ctx.send(embed=embed)
            return
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if role not in ctx.guild.roles: #if the role doesnt exist the bot creates one wiht default overwrites
            perms = discord.Permissions(add_reactions=False, send_messages=False, connect=False)
            await ctx.guild.create_role(name="Muted", permissions=perms)
            await member.add_roles(role)
            embed = discord.Embed(title=f"{member} has been muted")
            await ctx.send(embed=embed)
        else: #if its already made and the bot can access it
            await member.add_roles(role)
            embed = discord.Embed(title=f"{member} has been muted")
            await ctx.send(embed=embed)
  

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member=None):
        if member == None: #incase they dont mention a user
            #NOTE: THEY MUST BE MENTIONED 
            #EXAMPLE: @misaka#xxxx
            await ctx.send("Please specify a user!")
            return
        role = discord.utils.get(ctx.guild.roles, name="Muted")#find the role 'Muted'
        try:
            await member.remove_roles(role)
            await ctx.send(f"{member} sucessfully unmuted") #removes it
        except Exception:
            await ctx.send("That user isnt muted") #incase they arent muted

def setup(bot):
    bot.add_cog(moderation(bot))
    print("Moderation cog loaded\n----------\n")