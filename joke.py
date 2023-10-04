from discord.ext import commands
import random
import json
import asyncio
import requests
class joke_cog(commands.Cog):
  @commands.command(name="joke", help="Tells a joke")
  async def joke(self,ctx):
    response = requests.get("https://raw.githubusercontent.com/15Dkatz/official_joke_api/master/jokes/index.json")
    jokes_dict = json.loads(response.text)
    joke_id = random.randint(0,387)
    jokes=jokes_dict[joke_id]
    async with ctx.channel.typing():
      await asyncio.sleep(2)
    await ctx.send(jokes['setup'])
    await asyncio.sleep(5)
    async with ctx.channel.typing():
      await asyncio.sleep(2)
    await ctx.send(jokes['punchline'])