import csv

import discord
from discord.ext import commands
import re2 as re

from utils import utils


class MessageCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "expressions.csv"

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        Checks if messages sent in chat contain banned phrases, 
        by means of regular expressions.
        """
        if message.author.bot:
            return False

        expressions = utils.read_from_csv(self.file)

        for e in expressions:
            for i in e:
                if re.search(f"{i}", message.content):
                    channel = message.channel
                    await message.delete()
                    await channel.send(
                        message.author.mention + " please don't use that phrase here!"
                    )
