from discord.ext import commands

class Ping(commands.Cog):
  def __init__(self, bot):
        self.bot = bot

  @commands.Cog.listener()
  async def on_ready():
    print("Ping.py is ready!")
    
  @commands.command(name='ping')
  async def ping(self, ctx):
    pingLatency = round(self.bot.latency * 1000)  # Convert to milliseconds
    await ctx.send(f'Pong! Latency: {pingLatency}ms')

  @commands.command(name='pong')
  async def pong(self, ctx):
    pongLatency = round(self.bot.latency * 1000)
    await ctx.send(f'Ping! Latency: {pongLatency}ms')

async def setup(bot):
    await bot.add_cog(Ping(bot))
