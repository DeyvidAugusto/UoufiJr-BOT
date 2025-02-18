import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import aiohttp
import random
from datetime import datetime

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='opa')
async def opa(ctx):
    await ctx.send('Opa! Bão?')

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', check=check, timeout=5.0)
        if msg.content.lower() == 'bão' or msg.content.lower() == 'bao':
            await ctx.send('Então tá joia cumpadi! :D')
        elif msg.content.lower() == 'Bão dms uai':
            await ctx.send('Bom demais da conta sô!')
        else:
            ... # Não responda
    except asyncio.TimeoutError:
        ... # Não responda


@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send('Pong! Latência: {}ms'.format(latency))


@bot.command(name='sobre')
async def sobre(ctx):
    sobre = discord.Embed(
        title='Sobre o Bot',
        description='Bot criado por Deyvid Augusto. Github: https://github.com/DeyvidAugusto',
        color=discord.Color.purple()
    )
    sobre.add_field(name='Linguagem', value='Python', inline=False)
    sobre.add_field(name='Comandos', value='https://github.com/DeyvidAugusto/UoufiJr-BOT/blob/main/README.md', inline=False)
    sobre.set_footer(text='Bot em desenvolvimento')
    await ctx.send(embed=sobre)


@bot.command(name='uoufi')
async def uoufi(ctx):
    await ctx.send('Uoufi é o melhor programador da B3, além de ser o mais bonito e inteligente!')
    await asyncio.sleep(1.5)
    await ctx.send('Além de ser o mais POGGERS de todos! :O')


@bot.command(name='gato')
async def gato(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.thecatapi.com/v1/images/search') as resp:
            if resp.status == 200:
                data = await resp.json()
                await ctx.send(data[0]['url'])
            else:
                await ctx.send('Não consegui pegar uma imagem de gato no momento. Tente novamente mais tarde.')


@bot.command(name='cachorro')
async def cachorro(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.thedogapi.com/v1/images/search') as resp:
            if resp.status == 200:
                data = await resp.json()
                await ctx.send(data[0]['url'])
            else:
                await ctx.send('Não consegui pegar uma imagem de cachorro no momento. Tente novamente mais tarde.')


@bot.command(name='ban')
async def ban(ctx, member: discord.Member, *, reason=None):
    gifs = [
        'https://tenor.com/pt-BR/view/bongocat-banhammer-ban-hammer-bongo-gif-18219363',
        'https://tenor.com/pt-BR/view/ban-keyboard-gif-23575674',
        'https://tenor.com/pt-BR/view/doge-ban-hammer-doge-ban-doge-meme-meme-gif-17863422',
        'https://tenor.com/pt-BR/view/bane-no-banned-and-you-are-explode-gif-16047504'
    ]
    gif = random.choice(gifs)
    await ctx.send(f'{member.mention} foi EXPURGADO do servidor. {gif}')


@bot.command(name='fraseUoufolistica')
async def fraseUoufolistica(ctx, *, content: str):
    fraseUoufolistica = discord.Embed(
        title=f'Frase Uoufolística',
        description=content,
        color=discord.Color.blue(),
        timestamp=datetime.now()
    )
    fraseUoufolistica.set_footer(text='Todas as frases são pura GOZEIRA! (talvez nem todas)')
    fraseUoufolistica.set_image(url='https://i.kym-cdn.com/entries/icons/original/000/041/528/Young_Thug_-_Hot_ft._Gunna___Travis_Scott__Official_Music_Video__0-29_screenshot.png')
    await ctx.send(embed=fraseUoufolistica)

bot.run(TOKEN)