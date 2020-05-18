import os
from commands import message_check

import discord
from discord.ext import commands
import re2 as re

bot = commands.Bot(command_prefix="?")


@bot.event
async def on_ready():
    print(f"{bot.user.name} ready to roll")


#@bot.event
#async def on_message(message):
#    if re.search(r"\p{Greek}", message.content):
#        channel = message.channel
#        await channel.send("beep boop banned phrase")

bot.add_cog(message_check.MessageCheck(bot))

key = os.environ.get("DISCORD_TOKEN")
bot.run(key)
