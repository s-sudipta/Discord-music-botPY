from discord.ext import commands

class admin_cog(commands.Cog):
  @commands.command(name="mute", help="mute @user for 30 minutes")
  async def mute(ctx, member: discord.Member=None, time=None, *, reason=None):
    if not member:
	    await ctx.send("You must mention a member to mute!")
    elif not time:
	    await ctx.send("You must mention a time!")
    else:
	    if not reason:
   		  reason="No reason given"
    #Now timed mute manipulation
      try:
    	  seconds = time[:-1] #Gets the numbers from the time argument, start to -1
          duration = time[-1] #Gets the timed maniulation, s, m, h, d
        if duration == "s":
        	seconds = seconds * 1
        elif duration == "m":
        	seconds = seconds * 60
        elif duration == "h":
        	seconds = seconds * 60 * 60
        elif duration == "d":
        	seconds = seconds * 86400
        else:
        	await ctx.send("Invalid duration input")
          	return
    except Exception as e:
    	print(e)
        await ctx.send("Invalid time input")
        return
    guild = ctx.guild
   	Muted = discord.utils.get(guild.roles, name="Muted")
    if not Muted:
    	Muted = await guild.create_role(name="Muted")
        for channel in guild.channels:
        await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    await member.add_roles(Muted, reason=reason)
    muted_embed = discord.Embed(title="Muted a user", description=f"{member.mention} Was muted by {ctx.author.mention} for {reason} to {time}")
    await ctx.send(embed=muted_embed)
    await asyncio.sleep(seconds)
  	await member.remove_roles(Muted)
    unmute_embed = discord.Embed(title="Mute over!", description=f'{ctx.author.mention} muted to {member.mention} for {reason} is over after {time}")
    await ctx.send(embed=unmute_embed)