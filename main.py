import discord
import asyncio
import os

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

client = discord.Client(intents=intents)

TOKEN = os.environ.get("DISCORD_TOKEN")
VOICE_CHANNEL_ID = int(os.environ.get("VOICE_CHANNEL_ID"))

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    for guild in client.guilds:
        channel = guild.get_channel(VOICE_CHANNEL_ID)
        if channel and isinstance(channel, discord.VoiceChannel):
            # يدخل الروم الصوتي فقط
            await channel.connect()
            print(f"Connected to voice channel: {channel.name}")
            break

client.run(TOKEN)

