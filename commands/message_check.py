import csv

import discord
from discord.ext import commands
import re2 as re


class MessageCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "expressions.csv" 

        with open(self.file, "r", newline="\n") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            self.expressions = list(csv_data)

    @commands.Cog.listener()
    async def on_message(self, message):
        for e in self.expressions:
            if re.search(f"\{e}", message.content):
                channel = message.channel
                await channel.send("beep boop banned phrase")
