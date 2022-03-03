from discord.ext import commands

from settings import TOKEN
from utils import send_command

bot = commands.Bot(command_prefix="?", description="A bot for the Discord server")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.command()
async def whitelist(ctx, username: str):
    """Whitelists a user."""
    response = await send_command(f"whitelist add {username}")
    print(f"Whitelisting {username}")
    await ctx.send(response)


bot.run(TOKEN)
