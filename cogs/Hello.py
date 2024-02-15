from discord.ext import commands

class Hello(commands.Cog):
  def __init__(self, bot):
        self.bot = bot

  @commands.Cog.listener()
  async def on_ready():
    print("Hello.py is ready!")
    
  @commands.command(name='hello')
  async def ping(self, ctx):
    await ctx.send(f'Hello {ctx.author.name}, my name is Brian!')


async def setup(bot):
    await bot.add_cog(Hello(bot))