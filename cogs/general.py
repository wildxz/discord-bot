import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("🏓 Pong!")

    @commands.command()
    async def halo(self, ctx):
        await ctx.send(f"Halo, {ctx.author.mention}! Selamat datang di Dusun Pixel 🌾")

    @commands.command()
    async def sepibgt(self, ctx):
        await ctx.send(f"PALALU SEPI {ctx.author.mention}!")

async def setup(bot):
    await bot.add_cog(General(bot))
