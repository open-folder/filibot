import os
from datetime import datetime

import discord
import unidecode

from filibot_client import get_email_client
from filibot_translator import translate_last_message

client = discord.Client()
KEY_WORDS = ("-noticias massinhas", "/noticias massinhas", "$noticias massinhas", "!noticias-massinhas")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if unidecode.unidecode(message.content).lower().startswith(KEY_WORDS):
        print(
            f'Started search for last newsletter. User {message.author} at {datetime.today().strftime("%d/%m/%Y %H:%M:%S")}')
        email_client = get_email_client()
        email_client.select_folder('INBOX')
        messages = email_client.search(['FROM', 'newsletter@filipedeschamps.com.br'])
        response = email_client.fetch(messages, ['RFC822'])
        translated_message = translate_last_message(response)

    paragraphs = []
    for paragraph in translated_message.split('\n\n'):
        if len(paragraphs) == 0:
            paragraphs.append(paragraph)
        elif len(paragraphs[-1] + paragraph) < 2000:
            paragraphs[-1] = paragraphs[-1] + "\n\n" + paragraph
        else:
            paragraphs.append(paragraph)

    for paragraph in paragraphs:
        await message.channel.send(paragraph)



client.run(os.getenv("DISCORD_TOKEN"))
