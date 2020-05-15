import csv

import discord
from discord.ext import commands
import re2 as re


class AddDelExpressions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "expressions.csv"

        with open(file, "r", newline="\n") as e:
            self.expressions = csv.reader(e, delimiter=",")

    # @commands.command(name="add")
    # async def add_expression(self, ctx, expression):

    #    def is_valid(self, expression):
