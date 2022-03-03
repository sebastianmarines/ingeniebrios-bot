import os

from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("DISCORD_TOKEN")
RCON_HOST = os.getenv("RCON_HOST", "127.0.0.1")
RCON_PORT = os.getenv("RCON_PORT", 25575)
RCON_PASSWORD = os.getenv("RCON_PASSWORD", "password")
