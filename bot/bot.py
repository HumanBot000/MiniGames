import datetime
import random

import aiohttp
import nextcord
import asyncio
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

intents = nextcord.Intents().all()
bot = commands.Bot(command_prefix="Use slash commands", intents=intents)
color_blue = 0x3498db
color_red = 0xe74c3c
color_green = 0x2ecc71
color_orange = 0xc27a2c
guild_ids = [1063461326900445225]


@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    guild_count = 0
    async for guild in bot.fetch_guilds(limit=150):
        guild_count += 1
        print(f"{guild_count}. Server-Name: {guild.name}")
    print(f"Anzahl Server:  {guild_count}")


async def status_task():
    while True:
        await bot.change_presence(activity=nextcord.Game("/help"), status=nextcord.Status.online)
        await asyncio.sleep(15)
        await bot.change_presence(activity=nextcord.Game("In development"), status=nextcord.Status.online)
        await asyncio.sleep(15)


@bot.slash_command(description="shows you all commands", guild_ids=guild_ids, name="help")
async def help_command(interaction: Interaction):
    help_embed = nextcord.Embed(title="Commands:",
                                description="**/help** shows a view of all commands\n"
                                            "**/rock_paper_scissors** starts a new game\n"
                                            "**/slot** spins the slot machine\n"
                                            "**/coinflip** flip a coin",
                                color=0x3498db)
    await interaction.send(embed=help_embed)


@bot.slash_command(description="rock, paper, Scissors", guild_ids=guild_ids)
async def rock_paper_scissors(interaction: Interaction,
                              value: str = SlashOption(
                                  name="value",
                                  choices=["🪨Rock", "📄Paper", "✂Scissors"]
                              )):
    random_option = random.choice(["📄", "✂", "🪨"])
    rps_draw_embed = nextcord.Embed(title="You have a draw!",
                                    description=f"{value}  **:**  {random_option}",
                                    color=0xc27a2c)
    rps_win_embed = nextcord.Embed(title="You have won!",
                                   description=f"{value}  **:**  {random_option}",
                                   color=0x2ecc71)
    rps_lost_embed = nextcord.Embed(title="You have lost!",
                                    description=f"{value}  **:**  {random_option}",
                                    color=0xe74c3c)
    if value == random_option:
        await interaction.send(embed=rps_draw_embed)
    elif value == "📄" and random_option == "🪨" or value == "✂" and random_option == "📄" or value == "🪨" and \
            random_option == "✂":
        await interaction.send(embed=rps_win_embed)
    else:
        await interaction.send(embed=rps_lost_embed)


@bot.slash_command(description="spins the slot machine", guild_ids=guild_ids)
async def slot(interaction: Interaction):
    random_nums = []
    options = [":yellow_heart:", ":blue_heart:", ":green_heart:"]
    for i in range(3):
        random_nums.append(random.choice(options))
    slot_win_embed = nextcord.Embed(title="You have won!",
                                    description=f"[{random_nums[0]}][{random_nums[1]}][{random_nums[2]}]",
                                    color=0x2ecc71)
    slot_lose_embed = nextcord.Embed(title="You have lost!",
                                     description=f"[{random_nums[0]}][{random_nums[1]}][{random_nums[2]}]",
                                     color=0xe74c3c)
    if random_nums[0] == random_nums[1] and random_nums[1] == random_nums[2]:
        await interaction.send(embed=slot_win_embed)
    else:
        await interaction.send(embed=slot_lose_embed)


@bot.slash_command(description="See your ping", guild_ids=guild_ids)
async def ping(interaction):
    embed = nextcord.Embed(title="Ping? Pong!",
                           colour=nextcord.Colour(0xc44790), url="https://discordapp.com",
                           description=f"Pong 🏓{round(bot.latency * 1000, 1)}ms",
                           timestamp=datetime.datetime.utcfromtimestamp(1673626739))

    embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    # Todo Footer
    await interaction.send(embed=embed)


@bot.slash_command(description="Reddit Memes", guild_ids=guild_ids)
async def meme(interaction: Interaction,
                              thread: str = SlashOption(
                                  name="thread",
                                  choices=["dankmemes", "memes", "Programmerhumor", "deutschememes"]
                              )):
    embed = nextcord.Embed(colour=nextcord.Colour.random())
    async with aiohttp.ClientSession() as cs:
        try:
            async with cs.get(f'https://www.reddit.com/r/{thread}/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(
                    url=res['data']['children'][random.randint(0, len(res['data']['children']))]['data']['url'])
            embed.set_footer(text=f"r/{thread}")
        except Exception:
            embed = nextcord.Embed(colour=nextcord.Colour(color_red), title="Error please try again")
    await interaction.send(embed=embed)


@bot.slash_command(description="flip a coin", guild_ids=guild_ids)
async def coinflip(interaction: Interaction,
                   value: str = SlashOption(
                       name="value",
                       choices=["head", "tails"]
                   )):

    head_embed = nextcord.Embed(title="Coin flip", colour=nextcord.Colour.random(),
                           timestamp=datetime.datetime.now())

    head_embed.set_image(url="https://cdn.pixabay.com/photo/2018/04/29/19/47/five-3360941_960_720.jpg")
    head_embed.set_footer(text="flipping")
    # ----------------------------------------------------------------------------------------------
    tails_embed = nextcord.Embed(title="Coin flip", colour=nextcord.Colour.random(),
                           timestamp=datetime.datetime.now())

    tails_embed.set_image(url="https://cdn.pixabay.com/photo/2019/08/07/21/06/money-4391562_960_720.jpg")
    tails_embed.set_footer(text="flipping")
    msg = await interaction.send(embed=head_embed)
    for i in range(0, random.randint(3, 7)):
        await asyncio.sleep(1)
        await msg.edit(embed=tails_embed)
        await asyncio.sleep(1)
        await msg.edit(embed=head_embed)
    await asyncio.sleep(random.randint(2, 4))
    sites = ["Tails", "Heads"]
    random_choice = random.choice(sites)
    if random_choice == "Tails":
        await msg.edit(embed=tails_embed)
    else:
        await msg.edit(embed=head_embed)
    cf_win_embed = nextcord.Embed(title="You have won!",
                                  description=f":coin: {random_choice}",
                                  color=0x2ecc71)
    cf_lose_embed = nextcord.Embed(title="You have lost!",
                                   description=f":coin: {random_choice}",
                                   color=0xe74c3c)
    if random_choice == value:
        await interaction.send(embed=cf_win_embed)
    else:
        await interaction.send(embed=cf_lose_embed)


bot.run(token=open("token.txt", "r").read())
