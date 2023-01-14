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


# 0x3498db -->  blue
# 0xe74c3c -->  red
# 0x2ecc71 -->  green


async def status_task():
    while True:
        await bot.change_presence(activity=nextcord.Game("/hilfe"), status=nextcord.Status.online)
        await asyncio.sleep(15)
        await bot.change_presence(activity=nextcord.Game("In der Entwicklung"), status=nextcord.Status.online)
        await asyncio.sleep(15)


@bot.slash_command(description="Zeigt dir alle Befehle", guild_ids=guild_ids)
async def hilfe(interaction: Interaction):
    help_embed = nextcord.Embed(title="Befehle:",
                                description="**/help** zeigt eine Ansich aller Befehle\n"
                                            "**/rock_paper_scissors** startet ein neues Spiel\n"
                                            "**/slot** dreht an der Slotmaschine",
                                color=0x3498db)
    await interaction.send(embed=help_embed)


@bot.slash_command(description="Rock, Paper, Scissors ", guild_ids=guild_ids)
async def rock_paper_scissors(interaction: Interaction,
                              value: str = SlashOption(
                                  name="value",
                                  choices=["🪨", "📄", "✂"]
                              )):
    random_option = random.choice(["📄", "✂", "🪨"])
    if value == random_option:
        await interaction.send(f"Unentschieden {value}:{random_option}")
    elif value == "📄" and random_option == "🪨" or value == "✂" and random_option == "📄" or value == "🪨" and \
            random_option == "✂":
        await interaction.send(f"Gewonnen{value}:{random_option}")
    else:
        await interaction.send(f"Verloren  {value}:{random_option}")


@bot.slash_command(description="Drehe an der Slotmaschine", guild_ids=guild_ids)
async def slot(interaction: Interaction):
    random_nums = []
    options = [":yellow_heart:", ":blue_heart:", ":green_heart:"]
    for i in range(3):
        random_nums.append(random.choice(options))
    slot_win_embed = nextcord.Embed(title="Du hast gewonnen!",
                                    description=f"[{random_nums[0]}][{random_nums[1]}][{random_nums[2]}]",
                                    color=0x2ecc71)
    slot_lose_embed = nextcord.Embed(title="Du hast verloren!",
                                     description=f"[{random_nums[0]}][{random_nums[1]}][{random_nums[2]}]",
                                     color=0xe74c3c)
    if random_nums[0] == random_nums[1] and random_nums[1] == random_nums[2]:
        await interaction.send(embed=slot_win_embed)
    else:
        await interaction.send(embed=slot_lose_embed)


bot.run(token=open("token.txt", "r").read())
