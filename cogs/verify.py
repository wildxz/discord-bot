import discord
from discord.ext import commands
from discord.ui import Button, View
import json

# Load konfigurasi
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verifysetup(self, ctx):
        embed = discord.Embed(
            title="🔐 **VERIFIKASI DI BUTUHKAN!!**",
            description=(
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                "🔔 **Selamat Datang di** `Dusun Pixel`!\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "🚨 Demi menjaga keamanan komunitas, kamu **wajib melakukan verifikasi terlebih dahulu** sebelum mengakses seluruh channel.\n\n"
                "✅ Verifikasi ini hanya dilakukan **1x saja** dan akan memberikanmu akses sebagai **Warga Resmi**.\n\n"
                "▶️ Klik tombol **Verify** di bawah ini untuk memulai proses.\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
            color=discord.Color.gold()
        )

        verify_button = Button(label="Verify", style=discord.ButtonStyle.success, custom_id="verify_button")
        help_button = Button(label="Help", style=discord.ButtonStyle.secondary, custom_id="help_button")

        view = View()
        view.add_item(verify_button)
        view.add_item(help_button)

        verify_channel = self.bot.get_channel(config["verify_channel_id"])
        if verify_channel:
            await verify_channel.send(embed=embed, view=view)
        else:
            await ctx.send("Channel tidak ditemukan!")
        

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.data.get("custom_id") == "verify_button":
            verified_role = discord.utils.get(interaction.guild.roles, id=config["verify_role_id"])
            old_role = discord.utils.get(interaction.guild.roles, id=config["unverified_role_id"])
            
            if verified_role:
                #hapus role lama
                if old_role in interaction.user.roles:
                    await interaction.user.remove_roles(old_role)
                #menambah role baru
                    await interaction.user.add_roles(verified_role)
                    await interaction.response.send_message(
                        "✅ Kamu berhasil diverifikasi! Role lamamu telah diganti.", ephemeral=True
                    )    
            
        elif interaction.data.get("custom_id") == "help_button":
            support_channel_id = 1353606116751183875  # ganti sesuai channel ID kamu

            view = View()
            view.add_item(
                Button(
                emoji="🔗",
                label="Kunjungi Channel Bantuan",
                style=discord.ButtonStyle.link,
                url=f"https://discord.com/channels/{interaction.guild.id}/{support_channel_id}"
        )
    )

            await interaction.response.send_message(
            "🔧 Butuh bantuan? Hubungi staff atau klik tombol dibawah.",
            view=view,
            ephemeral=True
        )

# ✅ Gunakan async def setup (bukan def setup)
async def setup(bot):
    await bot.add_cog(Verify(bot))
    print("verify.py loaded!")
