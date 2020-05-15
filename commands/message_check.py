import csv

import discord
from discord.ext import commands
import re2 as re


class MessageCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "expressions.csv"

        with open(file, "r", newline="\n") as e:
            self.expressions = csv.reader(e, delimiter=",")

    @commands.Cog.listener()
    async def on_message(self, message):
        for e in self.expressions:
            if re.search(f'{e}', message.content):
                channel = message.channel
                await channel.send('beep boop banned phrase')



