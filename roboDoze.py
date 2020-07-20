#!/usr/bin/env python3
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
        
            
    print(
        f'{client.user} has connected to Discord!\n'
        f'{guild.name} ID: {guild.id}')

    members = '\n - '.join([members.name for members in guild.members])
    print(f'Members: \n {members}')

@client.event
async def on_member_join(member):
    channel = client.get_channel(734834110769659917)
    await channel.send(
        (f'Yo {member.name}, welcome to {GUILD}'
        'I\'m the resident server bot, type !help to get a list of commands')

    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'yo':
        greeting_response = ('sup')
        await message.channel.send(greeting_response)

@bot.command(name='help')
async def helpful(ctx):
    help_response = ('Naw dude, can\'t really help you yet...\n'
    'But, if you want to help me, go here: ')
    await ctx.send(help_response)

client.run(TOKEN) 