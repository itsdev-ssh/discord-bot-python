# código criado por ItsDev?_.

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Seu bot está online!')

# comando de !ola
@bot.command()
async def ola(ctx):
    await ctx.send(f"Olá, {ctx.author.mention}!")

TOKEN = "seu token" # cole seu token aqui.
bot.run(TOKEN)