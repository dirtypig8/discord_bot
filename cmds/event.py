import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(619786855675854848)
        await channel.send('{} join'.format(member))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(619786855675854848)
        await channel.send('{} leave'.format(member))

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == 'apple':
            await msg.channel.send('hi')


def setup(bot):
    bot.add_cog(Event(bot))