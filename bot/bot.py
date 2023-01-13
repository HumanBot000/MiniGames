import random

import nextcord
import asyncio
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

intents = nextcord.Intents().all()
bot = commands.Bot(command_prefix="Use slash commands", intents=intents)

guild_ids = [1063461326900445225]
@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    guild_count = 0
    async for guild in bot.fetch_guilds(limit=150):
        guild_count +=1
        print(guild.name)
    print(guild_count)


async def status_task():
        while True:
            await bot.change_presence(activity=nextcord.Game("/help"), status=nextcord.Status.online)
            await asyncio.sleep(15)
            await bot.change_presence(activity=nextcord.Game("In der Entwicklung"), status=nextcord.Status.online)
            await asyncio.sleep(15)


@bot.slash_command(description="Rock Paper Scissors ",guild_ids=guild_ids)
async def game_psr(interaction : Interaction,
                   value : str = SlashOption(
                       name = "value",choices=["🪨","📄","✂"]
                   )):
    random_option = random.choice(["📄","✂","🪨"])
    if value == random_option:
        await interaction.send(f"Unentschieden {value}:{random_option}")
    elif value == "📄" and random_option == "🪨" or value == "✂" and random_option == "📄" or value == "🪨" and random_option == "✂":
        await interaction.send(f"Gewonnen{value}:{random_option}")
    else:
        await interaction.send(f"Verloren  {value}:{random_option}")





bot.run(token=open("token.txt","r").read())

