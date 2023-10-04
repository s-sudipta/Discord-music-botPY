import discord
from discord.ext import commands
import random
import aiohttp

class meme_cog(commands.Cog):
  @commands.command(name="meme", help="to get a meme")
  async def meme(self,ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('http://www.reddit.com/r/memes.json') as r:
        memes = await r.json()
        embed = discord.Embed(
        color = discord.Color.purple()
      )
        embed.set_image(url=memes["data"]["children"][random.randint(0,25)]["data"]["url"])
        embed.set_footer(text=f"Powered by r/memes! | BelugaOP | meme requested by {ctx.author}")
        await ctx.send(embed=embed)