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
        guild_count += 1
        print(f"{guild_count}. Server-Name: {guild.name}")
    print(f"Anzahl Server:  {guild_count}")


# 0x3498db -->  blue   --> System
# 0xe74c3c -->  red    --> Lost
# 0x2ecc71 -->  green  --> Win
# 0xc27a2c -->  orange --> Draw


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
                                  choices=["🪨", "📄", "✂"]
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


@bot.slash_command(description="flip a coin", guild_ids=guild_ids)
async def coinflip(interaction: Interaction,
                   value: str = SlashOption(
                       name="value",
                       choices=["head", "tails"]
                   )):
    choices = ["head", "tails"]
    random_choice = random.choice(choices)
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
