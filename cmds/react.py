import discord
from discord.ext import commands
from core.classes import Cog_Extension


class React(Cog_Extension):
    @commands.command()
    async def web(self, ctx):
        url = 'https://scontent.ftpe3-2.fna.fbcdn.net/v/t1.0-9/10525786_771049469583114_4629975771234200608_n.jpg?_nc_cat=102&_nc_oc=AQl2ykJKC_crEXqOsxctyZGrbzC9McrCKCOHjwtXtZ7_hSL7Bo8KdG0-fgKN8r9QgR0&_nc_ht=scontent.ftpe3-2.fna&oh=3733ccf9cbabb9f93c7bbdbd747845b4&oe=5E067E73'
        await ctx.send(url)


def setup(bot):
    bot.add_cog(React(bot))