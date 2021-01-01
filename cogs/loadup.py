import discord
from discord.ext import commands
from os import system, name
from asyncio import sleep
import platform
import sys
from colorama import Fore, init

class Boot(commands.Cog):
    def __init__(self, bot, *args):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        async def status():
            while True:
                await self.bot.wait_until_ready()
                await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f'to {len(self.bot.users)} Users'))
                await sleep(15)
                await self.bot.change_presence(status=discord.Status.online ,activity=discord.Activity(type=discord.ActivityType.watching, name=f"My next updates...⏳"))
                await sleep(15)
                await self.bot.change_presence(status=discord.Status.online ,activity=discord.Activity(type=discord.ActivityType.listening, name='a police radio...'))
                await sleep(15)
                await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Catalyst early access"))
                await sleep(15)
        print(Fore.BLUE + 'All Cogs Loaded!\n---------\n' + Fore.RESET)
        print(Fore.GREEN + f'{sys.version}\n--------' + Fore.RESET)
        self.bot.loop.create_task(status())

def setup(bot):
    bot.add_cog(Boot(bot))
    print("Booter loaded\n--------\n")