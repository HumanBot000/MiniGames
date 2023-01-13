import datetime
import random

import nextcord
import asyncio
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

intents = nextcord.Intents().all()
bot = commands.Bot(intents=intents)

guild_ids = [1063461326900445225]


@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    guild_count = 0
    async for guild in bot.fetch_guilds(limit=150):
        guild_count += 1
        print(guild.name)
    print(guild_count)


async def status_task():
    while True:
        await bot.change_presence(activity=nextcord.Game("/help"), status=nextcord.Status.online)
        await asyncio.sleep(15)
        await bot.change_presence(activity=nextcord.Game("in development"), status=nextcord.Status.online)
        await asyncio.sleep(15)


@bot.slash_command(description="See your ping", guild_ids=guild_ids)
async def ping(interaction):
    embed = nextcord.Embed(title="Ping? Pong!",
                          colour=nextcord.Colour(0xc44790), url="https://discordapp.com",
                          description=f"Pong 🏓{round(bot.latency * 1000, 1)}ms",
                          timestamp=datetime.datetime.utcfromtimestamp(1673626739))

    embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    #Todo Footer
    await interaction.send(embed=embed)


@bot.slash_command(description="Rock Paper Scissors ", guild_ids=guild_ids)
async def game_psr(interaction: Interaction,
                   value: str = SlashOption(
                       name="value", choices=["🪨", "📄", "✂"]
                   )):
    random_option = random.choice(["📄", "✂", "🪨"])
    if value == random_option:
        text = f"Unentschieden {value}:{random_option}"
    elif value == "📄" and random_option == "🪨" or value == "✂" and random_option == "📄" or value == "🪨" and random_option == "✂":
        text = f"Gewonnen{value}:{random_option}"
    else:
        text = f"Verloren  {value}:{random_option}"
    embed = nextcord.Embed(title="Rock Paper Scissors",
                          colour=nextcord.Colour.random(), url="https://discordapp.com",
                          description=text,
                          timestamp=datetime.datetime.utcfromtimestamp(1673626739))

    embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    await interaction.send(embed=embed)
bot.run(token=open("token.txt", "r").read())
