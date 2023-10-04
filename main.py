import os
import discord
from discord.ext import commands
from joke import joke_cog
from music import music_cog
from meme import meme_cog
from hello import hello_cog
from hello import server_cog
#from nfsw import nsfw_cog
#from adminpower import admin_cog
from xkeep_alive import keep_alive
#client = discord.Client(intents=discord.Intents.default())
client = commands.Bot(intents=discord.Intents.all() , command_prefix= "?" , description='The Best Bot For the Best User!')
#client = commands.Bot(command_prefix="?")
global id
@client.event
async def on_ready():
    print('bot is ONLINE!!!! ')
    print(id)
    await client.add_cog(music_cog(client))
    await client.add_cog(joke_cog(client))
    await client.add_cog(meme_cog(client))
    await client.add_cog(hello_cog(client))
    await client.add_cog(server_cog(client))
#client.add_cog(admin_cog(client))
keep_alive()

client.run('0XI3hXjpkZIGAjVREW7HWcSxLgYo4VTK')
