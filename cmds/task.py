import discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio
from JavBus_fn import  Javbus
from Avgle_fn import Avgle
import random
Javbus_obj = Javbus()
avid_list = Javbus_obj.get_page_video(page_num='1')

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            channel = self.bot.get_channel(619784305157210123)
            while not self.bot.is_closed():
                avid = random.choice(avid_list)
                Avgle_obj = Avgle(avid)
                title = Avgle_obj.get_avid_information(key="title")
                embedded_url = Avgle_obj.get_avid_information(key="embedded_url")
                preview_video_url = Avgle_obj.get_avid_information(key="preview_video_url")
                img = Javbus_obj.get_avid_img(avid)
                message = '\n番號: {}\n名稱: {}\n{}\n完整連結:\n {}\n\n縮影:\n {}'.format(avid, title, img, embedded_url,preview_video_url)
                await channel.send(message)
                await asyncio.sleep(1000)

        self.bg_task = self.bot.loop.create_task(interval())

def setup(bot):
    bot.add_cog(Task(bot))