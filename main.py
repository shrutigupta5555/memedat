import discord 
from discord.embeds import Embed 
# from discord import client
from discord.ext import commands 

from dotenv import load_dotenv 
import os


bot = commands.Bot(command_prefix='!!')
load_dotenv()



@bot.command()
async def ping(ctx):
    await ctx.send('pong pong')


@bot.command()
async def prompt(ctx):
    await ctx.send_file('p')





bot.run(os.getenv('BOT_TOKEN'))