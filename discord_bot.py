import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)

forbidden_words = [
    "nigger", "Nigger", "n*gger", "n*gga", "n*gg@", "n*gg3r", "n*gg@r", "n*ggah", "n*gguh",
    "n1gger", "n1gga", "n1gg3r", "n1gg@r", "n1663r", "n166@r", "n166er", "n166ah", "n166uh",
    "n!gger", "n!gga", "n!gg3r", "n!gg@r", "n!ggah", "n!gguh", "nibber", "nibba", "nibb3r",
    "nibb@r", "nibbah", "nibbuh", "ni663r", "ni66@r", "ni66er", "ni66ah", "ni66uh", "nigg3r",
    "nigg@r", "niggah", "nigguh", "n!bber", "n!bba", "n!bb3r", "n!bb@r", "n!bbah", "n!bbuh",
    "n i g g e r", "n i g g a", "n i b b e r", "n i b b a", "n! g g e r", "n! g g a",
    "n! b b e r", "n! b b a", "n1gg3r", "n1bb3r", "n1bb@r", "n1bbah", "n1bbuh", "n!gg3r",
    "n!bb3r", "n!bb@r", "n!bbah", "n!bbuh", "faggot", "Faggot", "kys", "KYS", "fags"
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if random.random() < 0.001:
        await message.author.ban(reason="just ur luck")
        await message.channel.send(f"{message.author.mention} has been banned from Palme")
    else:
        warnings = ["Erste Verwarnung!", "Zweite Verwarnung!", "Dritte Verwarnung!"]
        warning = random.choice(warnings)
        await message.channel.send(f"{message.author.mention}, {warning}")

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))