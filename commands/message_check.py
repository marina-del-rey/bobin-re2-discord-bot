import csv

import discord
from discord.ext import commands
import re2 as re


class MessageCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "expressions.csv"

        with open(self.file, "r") as csv_file:
            csv_data = csv.reader(csv_file, delimiter="\n")
            self.expressions = list(csv_data)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return False

        for exp in self.expressions:
            for i in exp:
                if re.search("\{}".format(i), message.content):
                    channel = message.channel
                    await message.delete()
                    await channel.send(message.author.mention + " please don't use that phrase here!")
