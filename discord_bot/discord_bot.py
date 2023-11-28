import discord
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """
    This function is called when the bot is ready.
    It prints a message to the console indicating the bot has logged in.
    """
    print(f"Logged in as {bot.user.name}")
    my_background_task.start()  # Start the background task


@bot.command(name="hello")
async def hello(ctx):
    """
    Responds to the !hello command with a greeting.

    Args:
    ctx (discord.ext.commands.Context): The context in which the command was called.
    """
    await ctx.send("Hello there!")


@tasks.loop(minutes=1)
async def my_background_task():
    """
    This function represents a background task that runs every 60 minutes.
    """
    channel = bot.get_channel(CHANNEL_ID_INT)  # Replace with your channel ID
    if channel:
        await channel.send("1 minute has passed!")


@my_background_task.before_loop
async def before_my_task():
    """
    This function runs before the background task starts.
    It ensures that the bot is fully ready before the task begins.
    """
    await bot.wait_until_ready()


# Replace 'your_token_here' with your bot's token
bot.run("your_token_here")
