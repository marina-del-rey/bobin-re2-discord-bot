import os

import discord
from discord.ext import commands
import re2 as re

bot = commands.Bot(command_prefix="?")


@bot.event
async def on_ready():
    print(f"{bot.user.name} ready to roll")


key = os.environ.get("DISCORD_TOKEN")
bot.run(key)
