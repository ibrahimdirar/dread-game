import random
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

big_frightening_number = 100
death_count = 0
player_list = {}
player_stats = {}

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Succesfully connected to Discord!')

# Virtual tower initialise with a Big Frightening Number of 100. 
@bot.command(name='start', help='Initialises a game of dread')
async def initialise(ctx):
        global big_frightening_number
        big_frightening_number = 100
        await ctx.send(f'Big Frightening Number: {big_frightening_number}')
        global player_list
        global death_count
        death_count = 0
        player_list = {}
        await ctx.send('Please can each player type in "!join Character_Name"')

# Adds an entry to the player_list dictionary with Discord user key and character name value
@bot.command(name='join', help='Adds a character')
async def initialise(ctx, character_name):
        global player_list
        global player_stats
        player_list[ctx.author.name] = character_name
        player_stats[ctx.author.name] = 0
        await ctx.send(f'Added character {character_name} to {ctx.author.name}')

# Dumps the player_list dictionary into chat
@bot.command(name='characters', help='Lists all characters')
async def initialise(ctx):
        global player_list
        await ctx.send(player_list)

# Dumps the player_stats dictionary into chat - key: Discord user, value: cumulative number of pulls
@bot.command(name='stats', help='Lists all player stats')
async def initialise(ctx):
        global player_stats
        await ctx.send(player_stats)

# Handles pulling from the tower, the tower falling over and rebuilding the tower
@bot.command(name='pull', aliases=['draw','roll'], help='Pull from the tower, can supply a number for multiple pulls')
async def initialise(ctx, pulls: int=1):
        global big_frightening_number
        global player_list
        global death_count
        global player_stats
        await ctx.send(f'BFN: {big_frightening_number}')
        if ctx.author.name in player_list:
            for i in range(0, pulls):
                    roll_1 = random.randint(1,100)
                    roll_2 = random.randint(1,100)
                    await ctx.send(f'Roll {roll_1}, {roll_2}')
                    pull = min(roll_1, roll_2)
                    if pull > big_frightening_number:
                        await ctx.send(f'The tower has fallen!\n{ctx.author.name} has died!')
                        death_count += 1
                        player_list.pop(ctx.author.name)
                        if not player_list:
                            await ctx.send('All characters are dead!')
                        else:
                            big_frightening_number = 100
                            await ctx.send(f'Generating a new tower!\nAs {death_count} players have died, {death_count*3} pulls are required.')
                            drawing_list = player_list.copy()
                            for i in range(0,death_count*3):
                                    if not drawing_list:
                                        drawing_list = player_list.copy()
                                    drawing_player = drawing_list.pop(random.choice(list(drawing_list.keys())))
                                    await ctx.send(f'Player {drawing_player} must draw one')
                        break
                    else:
                        big_frightening_number-=(pull+9)//10
                        player_stats[ctx.author.name] += 1
                        await ctx.send(f'BFN: {big_frightening_number}')
            await ctx.send('Done')
        else:
            await ctx.send(f'{ctx.author.name}, you are currently not a player. Please use "!join Character_Name"')
bot.run(TOKEN)



        