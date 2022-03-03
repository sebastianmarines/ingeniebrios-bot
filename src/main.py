from discord.ext import commands
from rcon.source import rcon

from settings import RCON_HOST, RCON_PORT, RCON_PASSWORD, TOKEN


bot = commands.Bot(command_prefix="?", description="A bot for the Discord server")


async def _send_command(command: str) -> str:
    """
    Sends a command to the RCON server and returns the response.
    """
    response = await rcon(
        *command.split(), host=RCON_HOST, port=int(RCON_PORT), passwd=RCON_PASSWORD
    )

    return response


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.command()
async def whitelist(ctx, username: str):
    """Whitelists a user."""
    command = f"whitelist add {username}".split()
    response = await rcon(
        *command, host=RCON_HOST, port=int(RCON_PORT), passwd=RCON_PASSWORD
    )
    print(f"Whitelisting {username}")
    await ctx.send("Whitelisting...")


bot.run(TOKEN)
