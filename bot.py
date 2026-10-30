import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "V AI Bot is alive and running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! V AI is working 24/7 🚀')

keep_alive()

TOKEN = "MTU2NTcwMDQ0NTk4MzIxMTYzMA.G1H0Ee.NpNxdDOPAAfINCVpolkCcsdn31WyMHtcxYKO24"
bot.run(TOKEN)
