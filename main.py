import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='opa')
async def opa(ctx):
    await ctx.send('Opa!')