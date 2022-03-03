from rcon.source import rcon

from settings import RCON_HOST, RCON_PASSWORD, RCON_PORT


async def send_command(command: str) -> str:
    """
    Sends a command to the RCON server and returns the response.
    """
    response = await rcon(
        *command.split(), host=RCON_HOST, port=int(RCON_PORT), passwd=RCON_PASSWORD
    )

    return response
