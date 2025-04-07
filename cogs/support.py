import discord
from discord.ext import commands

class SupportResponder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        # Cek apakah ini channel teks dan nama mengandung "ticket"
        if isinstance(channel, discord.TextChannel) and "ticket" in channel.name.lower():
            try:
                await channel.send(
                    "👋 Halo! Tim kami akan segera membantu kamu.\n"
                    "Silakan jelaskan kendala atau pertanyaan kamu di sini ya 🙌"
                )
            except Exception as e:
                print(f"Gagal mengirim pesan otomatis ke {channel.name}: {e}")

async def setup(bot):
    await bot.add_cog(SupportResponder(bot))
    print("support.py loaded!")
