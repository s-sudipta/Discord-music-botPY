from discord.ext import commands
import random

 
class hello_cog(commands.Cog):
  @commands.command(name="hello", help="Greetings")
  async def hello(self,ctx):
    hello = ["olá", "নমস্কার", "नमस्ते","hello", "hola", "bonjour", "konnichiwa","Привет"]
    await ctx.send(random.choice(hello))
class server_cog(commands.Cog):
  @commands.command(name="server", help="display server id")
  async def server(self,ctx):
    await ctx.send("ID: {}".format(ctx.guild.id))
    await ctx.send("my voice id : {}".format(ctx.author.voice.channel.id))
    await ctx.send("my user id : {}".format(ctx.author.id))
    