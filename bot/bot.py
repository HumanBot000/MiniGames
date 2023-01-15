import asyncio
import datetime
import random

import aiohttp
import nextcord
from nextcord import Interaction, SlashOption, ButtonStyle
from nextcord.ext import commands
from nextcord.ui import Button, View

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
    all_commands = [c.name for c in bot.commands]
    all_commands.append("In development")
    all_commands.append("/help for more infos")
    while True:
        await bot.change_presence(activity=nextcord.Game(random.choice(all_commands)), status=nextcord.Status.online)
        await asyncio.sleep(random.randint(10,20))


@bot.slash_command(description="shows you all commands", guild_ids=guild_ids, name="help")
async def help_command(interaction: Interaction):
    help_embed = nextcord.Embed(title="Commands:",
                                description="**/help** shows a view of all commands\n"
                                            "**/rock_paper_scissors** starts a new game\n"
                                            "**/slot** spins the slot machine\n"
                                            "**/coinflip** flip a coin\n"
                                            "**/numberguess** guess the number in a specific range\n"
                                            "/approach_missle come as near as posible to the target.But be carefully\n"
                                            "**/meme** see memes from reddit",
                                color=0x3498db)
    await interaction.send(embed=help_embed)


@bot.slash_command(description="Guess a given number", guild_ids=guild_ids, name="numberguess")
async def gtn(interaction: Interaction,
              number: int,
              value: str = SlashOption(
                  name="range",
                  choices=["1-10", "1-100", "1-1000"]
              )):
    value = int(value.split("-")[1])
    random_number = random.randint(1, value)
    gtn_win_embed = nextcord.Embed(title="You have won!",
                                   description=f"You have won the nuber was: {random_number}!",
                                   color=color_green)
    gtn_lose_embed = nextcord.Embed(title="You have lost!",
                                    description=f"You have lost the nuber was: {random_number}!",
                                    color=color_orange)
    if random_number == value:
        await interaction.send(embed=gtn_win_embed)
    else:
        await interaction.send(embed=gtn_lose_embed)


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
    button = Button(label="Play Again", style=ButtonStyle.primary, emoji="🔁")
    button.callback = approach_missle
    view = View(timeout=300)
    view.add_item(button)
    if random_nums[0] == random_nums[1] and random_nums[1] == random_nums[2]:
        await interaction.send(embed=slot_win_embed,view=view)
    else:
        await interaction.send(embed=slot_lose_embed,view=view)


@bot.slash_command(description="See your ping", guild_ids=guild_ids)
async def ping(interaction):
    embed = nextcord.Embed(title="Ping? Pong!",
                           colour=nextcord.Colour(0xc44790), url="https://discordapp.com",
                           description=f"Pong 🏓{round(bot.latency * 1000, 1)}ms",
                           timestamp=datetime.datetime.utcfromtimestamp(1673626739))

    button = Button(label="Try Again", style=ButtonStyle.primary, emoji="🔁")
    button.callback = ping
    view = View(timeout=300)
    view.add_item(button)
    await interaction.send(embed=embed,view=view)


@bot.slash_command(description="Reddit Memes", guild_ids=guild_ids)
async def meme(interaction: Interaction,
               thread: str = SlashOption(
                   name="thread",
                   choices=["dankmemes", "memes", "Programmerhumor", "deutschememes"]
               )):
    if thread not in ["dankmemes", "memes", "Programmerhumor", "deutschememes"]:
        thread = "dankmemes"
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
    button = Button(label="Show another", style=ButtonStyle.primary, emoji="🔁")
    button.callback = meme
    view = View(timeout=300)
    view.add_item(button)
    await interaction.send(embed=embed, view=view)


@bot.slash_command(description="Kill your target", guild_ids=guild_ids)
async def approach_missle(interaction):
    global player_count
    player_count = 0

    async def rise(interaction):
        global player_count
        player_count += random.randint(1, 5)
        await run(player_count)

    async def end(interaction):
        button = Button(label="Play Again", style=ButtonStyle.primary, emoji="🔁")
        button.callback = approach_missle
        view = View(timeout=300)
        view.add_item(button)
        target_count = random.randint(1, 3)
        if target_count == 1:
            target_count = random.randint(17, 20)
        else:
            target_count = random.randint(20, 24)

        global player_count
        lose_embed = nextcord.Embed(title="You have lost!",
                                    description=f"you missed your target. Your target had {target_count} points",
                                    color=color_red)
        win_embed = nextcord.Embed(title="You have won!",
                                   description=f"You hit your target it had {target_count} points",
                                   color=color_green)
        if player_count > target_count:
            await interaction.send(embed=win_embed, view=view)
        else:
            await interaction.send(embed=lose_embed, view=view)

    rise_button = Button(label="Rise count by 1 to 5", style=ButtonStyle.primary, emoji="⬆")
    exit_button = Button(label="Compare to Target", style=ButtonStyle.secondary, emoji="🚪")
    rise_button.callback = rise
    exit_button.callback = end
    view = View(timeout=300)
    view.add_item(rise_button)
    view.add_item(exit_button)
    msg = await interaction.send(f"The maximum is 25,you have {player_count} what do you like to do?", view=view)

    async def run(player_count):
        if player_count > 25:
            button = Button(label="Play Again", style=ButtonStyle.primary, emoji="🔁")
            button.callback = approach_missle
            view = View(timeout=300)
            view.add_item(button)
            lose_embed = nextcord.Embed(title="You have lost!",
                                        description=f"You overloaded your missle.",
                                        color=color_red)
            await msg.delete()
            await interaction.send(embed=lose_embed, view=view)
        else:
            rise_button = Button(label="Rise count by 1 to 5", style=ButtonStyle.primary, emoji="⬆")
            exit_button = Button(label="Compare to Target", style=ButtonStyle.secondary, emoji="🚪")
            rise_button.callback = rise
            exit_button.callback = end
            view = View(timeout=300)
            view.add_item(rise_button)
            view.add_item(exit_button)
            await msg.edit(f"The maximum is 25,you have {player_count} what do you like to do?", view=view)


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
    button = Button(label="Play Again", style=ButtonStyle.primary, emoji="🔁")
    button.callback = coinflip
    view = View(timeout=300)
    view.add_item(button)
    if random_choice == value:
        await interaction.send(embed=cf_win_embed, view=view)
    else:
        await interaction.send(embed=cf_lose_embed, view=view)


bot.run(token=open("token.txt", "r").read())
