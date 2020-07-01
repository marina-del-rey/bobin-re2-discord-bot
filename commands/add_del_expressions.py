import csv

import discord
import re2 as re
from discord.ext import commands
from discord.ext.commands import has_permissions
from tabulate import tabulate

from utils import utils


class AddDelExpressions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file = "expressions.csv"

    @commands.command(name="addexp")
    @has_permissions(administrator=True)
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
    @has_permissions(administrator=True)
    async def del_expression(self, ctx, *args):
        """
        Allows user to delete expressions from the list of expressions by index.
        Removes the expression from the csv file.
        """
        count = 0
        removed_exps = []

        for e in args:
            if e is int:
                success = utils.remove_by_index(int(e), self.file)
            else:
                success = utils.remove_by_exp(e, self.file)
            if success:
                removed_exps.append(e)
                count += 1

        if count > 0:
            response = f"sucessfully removed {count} expression(s) : {removed_exps}"
        else:
            response = "no expressions were removed"

        await ctx.send(response)

    @commands.command(name="list")
    @has_permissions(administrator=True)
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
            "```"
            + "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ list of regular expressions ✧\n"
            + "```"
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
