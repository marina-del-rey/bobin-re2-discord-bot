import csv

import discord
from discord.ext import commands
import re2 as re


class AddDelExpressions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "expressions.csv"

        with open(file, "r") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            self.expressions = list(csv_data)

    @commands.command(name="add")
    async def add_expression(self, ctx, expression):
        count = 0
        
        #for exp in self.expressions:
        #    for i in exp:


