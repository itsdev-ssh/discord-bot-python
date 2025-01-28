# Simples codigo para ligar um bot do discord, codigo criado por ItsDev?_.

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('COLE_SEU_TOKEN_AQUI') # Cole o token do seu bot aqui.

client = discord.client()

@client.event
async def on_ready():
    print(f'{client.user} foi ligado com sucesso!')

# voce pode implementar mais coisas aqui em baixo
# Este pequeno codigo é uma mensagem de boas vindas que o bot manda no privado do usuario que acabou de entrar em seu servidor do discord.

# @client.event
# async def on_member_join(member):
#    await member.create_dm()
#    await member.dm_channel.send(
#        f'Hi {member.name}, welcome to my Discord server!'
#    )

# remova as "#" para este codigo de boas vindas funcionar.

client.run(TOKEN)

# Este é só um exemplo básico de um codigo para discord bot em Python.