# bot.py

import os
import random
import json
from dotenv import load_dotenv
from difflib import get_close_matches

import discord
from discord.ext import commands

with open('../data/games_names.json') as f:
    GAMES_NAMES = json.load(f)

with open('../data/games_links.json') as f:
    GAMES_LINKS = json.load(f)

with open('../data/games_help.json') as f:
    GAMES_HELP = json.load(f)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='game', help="Gets a list of Games for Game Night")
async def game(ctx, game, info):
    if game is "help":
        res = ("Usage: `!game <name_of_the_game> <info/link>`\n" + 
        "For example, try: `!game cah info` or `!game keep_talking link`\n\n" +
        "Available games:\n\t" + "\n\t{}".join(GAMES_NAMES.items()))    
    await ctx.send(res)

@bot.command(name='roll', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='rool')
async def rool(ctx):
    pass

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
    if isinstance(error, commands.errors.CommandNotFound):
        incorrect_command = error.args[0].split()[1]
        all_commands = []
        for command in bot.commands:
            all_commands.append(command.name)
        helptext='`'+ incorrect_command + '` command not found. Closest matches: '
        helptext+= '`' + '`, `'.join(get_close_matches(incorrect_command, all_commands, cutoff=.3)) 
        helptext+= '`' 
        await ctx.send(helptext)

# @bot.command(name='create-channel')
# @commands.has_role('admin')
# async def create_channel(ctx, channel_name='real-python'):
#     guild = ctx.guild
#     existing_channel = discord.utils.get(guild.channels, name=channel_name)
#     if not existing_channel:
#         print(f'Creating a new channel: {channel_name}')
#         await guild.create_text_channel(channel_name)

bot.run(TOKEN)

# client = discord.Client()

# @client.event
# async def on_ready():
#     guild = discord.utils.find(lambda x: x.name == GUILD, client.guilds)
#     # guild = discord.utils.get(client.guilds, name=GUILD)

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})\n'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if str(message.content).startswith('!'):
#         response = "Responding!"
#         await message.channel.send(response)
#     elif message.content == 'raise-exception':
#         raise discord.DiscordException

# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise

"""Creating a subclass of client and overriding handler methods"""
# class CustomClient(discord.Client):
#     async def on_ready(self):
#         print(f'{self.user} has connected to Discord!')
# client = CustomClient()

# client.run(TOKEN)