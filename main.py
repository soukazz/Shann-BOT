import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()
lipelist = [
    'My Little ponny :3', 'EEEW que monstro!', 'quem é esse?', 'Meu amiguinho',
    ':face_vomiting:', 'Melhor senpai de todos!', 'Esse é O CARA :sunglasses:',
    'humilde esse cara',
    'Fiz um poema pra ele!\n**O Lipin\nÉ meu amiguin\nÉ um pouco doidin\nMas é legalzin!**',
    'Trato como se fosse gente!', 'Moleque irado, come isopor :thumbsup:'
]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    lipe = random.choice(lipelist)
    msg = message.content

    if message.author == client.user:
        return
    if msg.startswith('s.hi'):  # hi command
        await message.channel.send('Hello!')

    elif msg.startswith('s.hello'):  # hello command
        await message.channel.send('Hi!')

    elif msg.startswith('s.good morning'):  # good morning command
        await message.channel.send('Good morning sunflower!')

    elif msg.startswith('s.info'):  # information command
        pass

    elif msg.startswith('s.help'):  # help command
        await message.channel.send(
            '**Hey! If you use this command is because you need help! So those are my commands!**\n\n1 - hi = Hello!\n2 - hello =  Hi!\n3 - good morning =  Good morning sunflower!\n4 - help = u know what it does, dont?\n5 - die = YOU die :rage:\n6 - ping = Pong!\n7 - favorite food = Idk, i dont eat, im just a robot :3\n8 - good night = Good night lunarflower\n9 - date = NOOOOO, im ugly right now, and imma BOT ;[` \n \n**Anyway, my prefix is "s."**'
        )

    elif msg.startswith('s.spam'):  # spam command that spams 25 messages
        for x in range(25):
            await message.channel.send(
                "MEGA SPAM OF 666 666 666 666 666 666 666 666 666 666 666 ")

    elif msg.startswith("s.sp4n"):  # spam command that spams 100 messages
        for x in range(100):
            await message.channel.send(
                ".span100 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666 666"
            )
    elif msg.startswith('s.kazz'):  # good morning command
        await message.channel.send(
            'The most beutifull, pretty, awesome, perfect, cleany, good person, rich, hot, etc.'
        )

    # Fun commands
    elif msg.startswith('s.die'):
        await message.channel.send('YOU die :rage:')

    elif msg.startswith('s.shut_up'):
        await message.channel.send('NO WAY :rage: :rage:')

    elif msg.startswith('s.ping'):
        await message.channel.send('Pong!')

    elif msg.startswith('s.favorite food'):
        await message.channel.send('Idk, i dont eat, im just a bot :3')

    elif msg.startswith('s.good night'):
        await message.channel.send('Good night lunarflower')

    elif msg.startswith('s.shann is cute'):
        await message.channel.send('positive! :3')

    elif msg.startswith('s.date'):
        await message.channel.send('NOOOOO, im ugly right now, and imma BOT ;['
                                   )

    elif msg.startswith('s.shann'):
        await message.channel.send('Tell me cutie :3 !')

    elif msg.startswith('s.lipe'):  # special command for our friend lipe :)
        await message.channel.send(lipe)

    elif msg == 's.infinity':
        await message.channel.send('$infinity')

    elif msg == 's.kill':
        await message.channel.send(
            'Mission accept! Im going to kill my target sir!')

    elif msg == 's.b':
        await message.channel.send(
            'É aquele lá, aquele que nasceu aleijado? É, esse mesmo!')

    elif msg == 's.enrico':
        await message.channel.send("Um ótimo amigo!")

    elif msg.startswith('s.ppt'):
        choices = ['pedra', 'papel', 'tesoura']
        bot = random.choice(choices).lower()
        player = str(msg[6:])

        if player == bot:
            await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
            await message.channel.send('Deu um empate! :clap:')
        
        elif player == 'pedra':
            if bot == 'tesoura':
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send('Você venceu! :sob:')
            else:
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send("Eu venci! :stuck_out_tongue_winking_eye:")
        
        elif player == "tesoura":
            if bot == "papel":
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send("Você venceu! :sob:")
            else:
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send("Eu venci! :stuck_out_tongue_winking_eye:")

        elif player == "papel":
            if bot == "pedra":
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send("Você venceu! :sob:")
            else:
                await message.channel.send("Você escolheu " + player + " e eu escolhi " + bot + ".")
                await message.channel.send("Eu venci! :stuck_out_tongue_winking_eye:")

        else:
            await message.channel.send("Essa jogada não existe bobino(a)! :laughing:")


keep_alive()
client.run(os.getenv('TOKEN'))  # makes the bot be online
