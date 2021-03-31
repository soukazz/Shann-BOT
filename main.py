import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('.hi'):
    await message.channel.send('Hello!')
  elif message.content.startswith('.hello'):
    await message.channel.send('Hi!')
  elif message.content.startswith('.good morning'):
    await message.channel.send('Good morning sunflower!')

client.run(os.getenv('TOKEN'))