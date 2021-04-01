import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

lipe = ['My Little ponny :3', 'EEEW que monstro!']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    lipe = [
        'My Little ponny :3', 'EEEW que monstro!', 'quem é esse?',
        'Meu amiguinho', ':face_vomiting:', 'Melhor senpai de todos!',
        'Esse é O CARA :sunglasses:', 'humilde esse cara',
        'Fiz um poema pra ele!\n**O Lipin\nÉ meu amiguin\nÉ um pouco doidin\nMas é legalzin!**',
        'Trato como se fosse gente!', 'Moleque irado, come isopor :thumbsup:'
    ]
    lipe = random.choice(lipe)
    if message.author == client.user:
        return
    if message.content.startswith('.hi'):  # hi command
        await message.channel.send('Hello!')

    elif message.content.startswith('.hello'):  # hello command
        await message.channel.send('Hi!')

    elif message.content.startswith('.good morning'):  # good morning command
        await message.channel.send('Good morning sunflower!')

    elif message.content.startswith('.info'):  # information command
        pass

    elif message.content.startswith('.help'):  # help command
        await message.channel.send(
            '**Hey! If you use this command is because you need help! So those are my commands!**\n\n`1 - hi = Hello!\n2 - hello =  Hi!\n3 - good morning =  Good morning sunflower!\n4 - help = u know what it does, dont?\n5 - .die = YOU die :rage:\n6 - .ping = Pong!\n7 - .favorite food = Idk, i dont eat, im just a robot :3\n8 - .good night = Good night lunarflower\n9 - .date = NOOOOO, im ugly right now, and imma BOT ;[` \n \n**Anyway, my prefix is "."**'
        )

    elif message.content.startswith(
            '.spam'):  # spam command that spams 25 messages
        for x in range(25):
            await message.channel.send(
                "MEGA SPAM OF 666 666 666 666 666 666 666 666 666 666 666 ")

    elif message.content.startswith(
            ".sp4n"):  # spam command that spams 100 messages
        for x in range(100):
            await message.channel.send(
                ".span100 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666"
            )
    elif message.content.startswith('.kazz'):  # good morning command
        await message.channel.send(
            'The most beutifull, pretty, awesome, perfect, cleany, good person, rich, hot, etc.'
        )

    # Fun commands
    elif message.content.startswith('.die'):
        await message.channel.send('YOU die :rage:')

    elif message.content.startswith('.shut up'):
        await message.channel.send('NO WAY :rage: :rage:')

    elif message.content.startswith('.ping'):
        await message.channel.send('Pong!')

    elif message.content.startswith('.favorite food'):
        await message.channel.send('Idk, i dont eat, im just a bot :3')

    elif message.content.startswith('.good night'):
        await message.channel.send('Good night lunarflower')

    elif message.content.startswith('.shann is cute'):
        await message.channel.send('positive! :3')

    elif message.content.startswith('.date'):
        await message.channel.send('NOOOOO, im ugly right now, and imma BOT ;['
                                   )

    elif message.content.startswith('.shann'):
        await message.channel.send('Tell me cutie :3 !')

    elif message.content.startswith(
            '.lipe'):  # special command for our friend lipe :)
        await message.channel.send(lipe)

    elif message.content == '.infinity':
        await message.channel.send('$infinity')

    elif message.content == '.kill':
        await message.channel.send(
            'Mission accept! Im going to kill my target sir!')

    elif message.content == '.b':
        await message.channel.send(
            'É aquele lá, aquele que nasceu aleijado? É, esse mesmo!')

    elif message.content == '.enrico':
        await message.channel.send("Um ótimo amigo!")


keep_alive()
client.run(os.getenv('TOKEN'))  # makes the bot be online
