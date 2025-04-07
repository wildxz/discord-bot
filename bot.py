import discord
import os
import json
import logging
from discord.ext import commands

# Load config dari JSON
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# Bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

# Logging setup
logging.basicConfig(
    level=logging.ERROR,
    format='[%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("bot_error.log")
    ]
)

# Saat bot siap
@bot.event
async def on_ready():
    print(f'Bot aktif sebagai {bot.user}')

# Load semua cogs
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded: {filename}")

# Run bot
async def main():
    await load_cogs()
    await bot.start(config["token"])

import asyncio
asyncio.run(main())
