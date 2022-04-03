from random import randint
import discord 
from discord.embeds import Embed 
# from discord import client
from discord.ext import commands 

from dotenv import load_dotenv 
import os


bot = commands.Bot(command_prefix='~')
load_dotenv()

@bot.command()
async def ping(ctx):
    await ctx.send('pong pong')


@bot.command()
async def start(ctx):
    await ctx.send('tag all the players playing the game 😏')

    members = await bot.wait_for("message")
    m = members.content.split(" ")

    r = randint(0,30)
    filepath = f"templates/{r}.jpg"
    await ctx.send(file=discord.File(filepath))





bot.run(os.getenv('BOT_TOKEN'))