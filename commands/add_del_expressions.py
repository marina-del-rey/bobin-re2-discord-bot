import csv

import discord
from discord.ext import commands
import re2 as re


class AddDelExpressions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "expressions.csv"

        with open(self.file, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter="\n")
            self.expressions = list(reader)

    @commands.command(name="addexp")
    async def add_expression(self, ctx, *args):
        """
        Allows user to add an expression to list of ones used for checking messages.
        Writes said expression to the csv file of expressions.
        """
        def was_already_added(exp):
            for e in exp:
                for i in e:
                    if i not in self.expressions or valid_exp:
                        return False

        count = 0
        valid_exp = []
        for e in args:
            if not was_already_added(e):
                print(valid_exp)
                valid_exp.append(e)
                count += 1

        response = f"sucessfully added {count} expression(s)!"
        await ctx.send(response)
