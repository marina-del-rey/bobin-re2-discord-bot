import csv

import discord
from discord.ext import commands
import re2 as re
from tabulate import tabulate

from utils import utils


class AddDelExpressions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "expressions.csv"

    @commands.command(name="addexp")
    async def add_expression(self, ctx, *args):
        """
        Allows user to add expressions to the list of ones used for checking messages.
        Writes said expression to the csv file.
        """
        count = 0

        for e in args:
            success = utils.append_to_csv(e, self.file)
            if success:
                count += 1

        if count > 0:
            response = f"sucessfully added {count} expression(s)!"
        else:
            response = "no expressions were added"

        await ctx.send(response)

    @commands.command(name="delexp")
    async def del_expression(self, ctx, *args):
        """
        Allows user to delete expressions from the list of expressions.
        Removes the expression from the csv file.
        """
        count = 0
        removed_exps = []
        expressions = utils.read_from_csv(self.file)

        for e in args:
            in_file = utils.expression_already_in_file(e, self.file)
            if in_file:
                if utils.remove_from_csv(e, self.file):
                    removed_exps.append(e)
                    count += 1

        if count > 0:
            reponse = f"sucessfully removed {count} expression(s) : {removed_exps}"
        else:
            response = "no expressions were removed"
        
        await ctx.send(response)

    @commands.command(name="list")
    async def list_expressions(self, ctx):
        """
        Lists the expressions in the csv file in table form.
        Dms it to the user.
        """
        expressions = utils.read_from_csv(self.file)
        table = (e for e in expressions)
        headers = ["i", "expression"]
        user = ctx.message.author

        await user.send(
            "list of expressions"
            + "```"
            + tabulate(
                table,
                headers,
                showindex=True,
                tablefmt="presto",
                colalign=("center", "left"),
            )
            + "```"
        )
