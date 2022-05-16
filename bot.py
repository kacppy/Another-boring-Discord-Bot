import nextcord
from nextcord.ext import commands
import aiohttp
import random

channel_id = 123456789
dc_token = "token_here"


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_message_delete(self, message):
        myChannel = bot.get_channel(channel_id)
        if message.attachments and message.content:
            await bot.loop.create_task(myChannel.send('{0.author} has deleted the message: {0.content} {0.attachments[0].url}'.format(message)))
        elif message.attachments:
            await bot.loop.create_task(myChannel.send('{0.author} has deleted the message: {0.attachments[0].url}'.format(message)))
        else:
            await bot.loop.create_task(myChannel.send('{0.author} has deleted the message: {0.content}'.format(message)))


async def deleteme(ctx):
    msg = await ctx.send("I will delete myself now...")
    await msg.delete()



bot = Bot(command_prefix="!")

@bot.command()
async def memes(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://meme-api.herokuapp.com/gimme')
      memejson = await request.json()

   embed = nextcord.Embed(title="Here is your memes:", color=nextcord.Color.red())
   msg = f"[Click]({memejson['postLink']})"
   embed.add_field(name='Link:', value=msg)
   embed.set_image(url=memejson['url'])

   await ctx.send(embed=embed)


@bot.command()
async def anime(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.post('https://pic.re/image')
      animejson = await request.json()

   embed = nextcord.Embed(title="Random anime just for you ;*", color=nextcord.Color.red())
   msg = f"[Click]({animejson['file_url']})"
   embed.add_field(name='Link:', value=msg)
   embed.set_image(url=animejson['file_url'])

   await ctx.send(embed=embed)


@bot.command()
async def game(ctx):
    game_val = random.choice(["rock", "paper", "scissors"])
    await ctx.reply(game_val)



bot.run(dc_token)