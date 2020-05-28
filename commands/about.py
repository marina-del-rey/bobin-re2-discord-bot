import discord
from discord.ext import commands


class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="about")
    async def about(self, ctx):
        """
        Just explains bot's purpose and 
        lists all available commands.
        """
        embed = discord.Embed(
            title="★ about bobin bot ★",
            description="this bot was made to make bonin's life easier, by using google's re2 engine to ban certain phrases/alphabets from discord chat. it allows the addition of custom expressions, which will be used for checking messages. ^-^",
            color=0xE6B0D6,
        )
        embed.set_author(
            name="made by marina with ♡", icon_url="https://i.imgur.com/0EdhsIN.png"
        )
        embed.add_field(
            name="?addexp [*args]",
            value="lets user add expressions to the list of expressions checked.",
            inline=True,
        )
        embed.add_field(
            name="?delexp [*args]",
            value="lets user delete expressions from the list of expressions checked.",
            inline=True,
        )
        embed.add_field(
            name="?list",
            value="sends the user a direct message with a list of all the expressions used by the bot.",
            inline=True,
        )
        await ctx.send(embed=embed)
