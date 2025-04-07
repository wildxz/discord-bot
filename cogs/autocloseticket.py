import discord
from discord.ext import commands, tasks
import asyncio

class TicketAutoClose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_tickets = {}

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if isinstance(channel, discord.TextChannel) and "ticket" in channel.name.lower():
            self.active_tickets[channel.id] = 0
            await channel.send("📩 Halo! Channel ini akan otomatis ditutup jika tidak ada aktivitas selama 2 jam kedepan.")

            await self.monitor_channel(channel)

    async def monitor_channel(self, channel):
        def check(msg):
            return msg.channel.id == channel.id

        try:
            while True:
                await self.bot.wait_for("message", check=check, timeout=7200)  # uabh timeoutnya sesuai yg di inginkan persecond
        except asyncio.TimeoutError:
            await channel.send("⏳ Tidak ada aktivitas selama 2 jam. Channel ini akan ditutup.")
            await asyncio.sleep(10)
            await channel.delete()

    @commands.command(name="close")
    async def manual_close(self, ctx):
        if "ticket" in ctx.channel.name.lower():
            await ctx.send("🔒 Ticket ditutup oleh pengguna. Channel akan dihapus dalam 5 detik.")
            await asyncio.sleep(5)
            await ctx.channel.delete()

async def setup(bot):
    await bot.add_cog(TicketAutoClose(bot))
