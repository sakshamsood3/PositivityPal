import discord
import os
import requests
import json
import random
from replit import db
from keepalive import keep_alive

if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
    db["encouragements"] = encouragements


def read_text_file(filename):
    word_list = []

    with open(filename, 'r', encoding='latin-1') as file:
        for line in file:
            words = line.split()
            word_list.extend(words)

    return word_list


file_path = 'nw.txt'
sad_words = read_text_file(file_path)
print(sad_words)

encouraging_messages = [
    "You've got this!", "Believe in yourself and all that you are.",
    "You are capable of amazing things.",
    "Keep pushing forward, even when it's tough.",
    "You're making progress, no matter how small.",
    "You have the power to create positive change.",
    "Embrace the challenges and grow stronger.",
    "Every day is a new opportunity to shine.",
    "Your hard work will pay off in the end.",
    "Stay focused and never give up on your dreams.",
    "You are stronger than you think you are.",
    "You have the ability to overcome any obstacle.",
    "Remember why you started and let it fuel you.",
    "You are deserving of all the good things in life.",
    "Keep going, even if it feels difficult.",
    "You are making a difference in the world.", "Your potential is limitless.",
    "You are on the right track. Keep moving forward.",
    "Don't be afraid to take risks and step outside your comfort zone.",
    "You are capable of great things. Believe in yourself!",
    "Stay positive and keep a smile on your face.",
    "You are amazing just the way you are.",
    "You are braver than you believe, stronger than you seem, and smarter than you think.",
    "The best is yet to come. Keep going!",
    "You have what it takes to succeed. Trust yourself.",
    "Don't give up. Great things take time.",
    "You are an inspiration to others.",
    "The world needs your unique talents and gifts.",
    "You are enough. Remember that always.",
    "You have the power to change your life for the better.",
    "You are a great person / bot!"
]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('$hi'):
        await message.channel.send('Hello I am Your Positive Pal!')

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if db["responding"]:
        options = encouraging_messages
        if "encouragements" in db.keys():
            options = options + list(db["encouragements"])

    if any(word.lower() in msg.lower().split() for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragment(index)
            encouragements = list(db["encouragements"])
        await message.channel.send(encouragements)

    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
