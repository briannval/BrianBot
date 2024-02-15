import asyncio
import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
BOT_TOKEN = os.environ['DISCORD_BOT_SECRET']

@bot.event
async def on_ready():
    print("BrianBot is in")
    print(bot.user)

async def load():
  await bot.load_extension("cogs.Ping")
  await bot.load_extension("cogs.Hello")

async def main():
  async with bot:
    await load()
    await bot.start(BOT_TOKEN)

asyncio.run(main())