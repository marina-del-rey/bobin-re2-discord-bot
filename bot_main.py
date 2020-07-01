import os
from commands import message_check, add_del_expressions

import discord
from discord.ext import commands
import re2 as re

bot = commands.Bot(command_prefix="?")


@bot.event
async def on_ready():
    print(f"{bot.user.name} ready to roll")
    print("greetings from marina")
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game("with kat")
    )


bot.add_cog(message_check.MessageCheck(bot))
bot.add_cog(add_del_expressions.AddDelExpressions(bot))

key = os.environ.get("DISCORD_TOKEN")
bot.run(key)
