import discord
import os

DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('hi'):
        await message.channel.send('Hello!')
 
client.run(DISCORD_BOT_TOKEN)