import discord
import os
from replit import db
from keep_alive import keep_alive

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

  elif message.content.startswith('.help'):
    await message.channel.send('Hey! If you use this command is because you need help! So those are my commands!\n**1 - hi = Hello!\n2 - hello =  Hi!\n3 - good morning =  Good morning sunflower!\n4 - help = u know wha it does, dont?**\n My prefix is "."')

  elif message.content.startswith('.spam'):
        for x in range(25):
          await message.channel.send("MEGA SPAM OF 666 666 666 666 666 666 666 666 666 666 666 ")

  elif message.content.startswith(".span 100"):
        for x in range(100):
            await message.channel.send(".span100 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666")
            
  elif message.content.startswith('.die'):
    await message.channel.send('YOU die :rage:')

  elif message.content.startswith('.shut up'):
    await message.channel.send('NO WAY :rage: :rage:')

  elif message.content.startswith('.ping'):
    await message.channel.send('Pong!')    

  elif message.content.startswith('.favorite food'):
    await message.channel.send('Idk, i dont eat, im just a robot :3')

  elif message.content.startswith('.good night'):
    await message.channel.send('Good night lunarflower')
    
  elif message.content.startswith('.shann is cute'):
    await message.channel.send('positive! :3')

  elif message.content.startswith('.date'):
    await message.channel.send('NOOOOO, im ugly right now, and imma BOT ;[')

  elif message.content.startswith('.shann'):
    await message.channel.send('Tell me cutie :3 !')


keep_alive
client.run(os.getenv('TOKEN'))
