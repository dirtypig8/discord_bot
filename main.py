import discord
from discord.ext import commands
from JavBus_fn import  Javbus
from Avgle_fn import Avgle
import random
import os

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension('cmds.{}'.format(extension))
    await ctx.send('Loaded {} done.'.format(extension))

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension('cmds.{}'.format(extension))
    await ctx.send('UnLoaded {} done.'.format(extension))

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension('cmds.{}'.format(extension))
    await ctx.send('ReLoaded {} done.'.format(extension))

@bot.command()
async def av(ctx):
    avid = random.choice(avid_list)
    Avgle_obj = Avgle(avid)
    title = Avgle_obj.get_avid_information(key="title")
    embedded_url = Avgle_obj.get_avid_information(key="embedded_url")
    preview_video_url = Avgle_obj.get_avid_information(key="preview_video_url")
    img = Javbus_obj.get_avid_img(avid)
    message = '\n番號: {}\n名稱: {}\n{}\n完整連結:\n {}\n\n縮影:\n {}'.format(avid, title, img, embedded_url, preview_video_url)
    await ctx.send(message)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension('cmds.{}'.format(filename[:-3]))

if __name__ == '__main__':
    Javbus_obj = Javbus()
    avid_list = Javbus_obj.get_page_video(page_num='1')
    bot.run('NjE5NzgwMDg0MDY4MjUzNjk2.XXNO0g.9S1HQtG1ZweuwZ4Set5azjBiecc')

