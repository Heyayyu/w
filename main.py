import discord
from discord.ext import commands
from jikanpy import Jikan
import random

# Initialize bot and Jikan API client
bot = commands.Bot(command_prefix='!')
jikan = Jikan()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def anime(ctx, *, query):
    """Fetches anime details based on query."""
    try:
        search_result = jikan.search('anime', query)
        if search_result['results']:
            anime = search_result['results'][0]
            title = anime['title']
            synopsis = anime['synopsis']
            url = anime['url']
            response = f"**{title}**\n{synopsis}\nMore info: {url}"
        else:
            response = "No anime found with that name."
    except Exception as e:
        response = f"Error: {str(e)}"
    await ctx.send(response)

@bot.command()
async def manga(ctx, *, query):
    """Fetches manga details based on query."""
    try:
        search_result = jikan.search('manga', query)
        if search_result['results']:
            manga = search_result['results'][0]
            title = manga['title']
            synopsis = manga['synopsis']
            url = manga['url']
            response = f"**{title}**\n{synopsis}\nMore info: {url}"
        else:
            response = "No manga found with that name."
    except Exception as e:
        response = f"Error: {str(e)}"
    await ctx.send(response)

@bot.command()
async def character(ctx, *, query):
    """Fetches character details based on query."""
    try:
        search_result = jikan.search('character', query)
        if search_result['results']:
            character = search_result['results'][0]
            name = character['name']
            about = character['about']
            url = character['url']
            response = f"**{name}**\n{about}\nMore info: {url}"
        else:
            response = "No character found with that name."
    except Exception as e:
        response = f"Error: {str(e)}"
    await ctx.send(response)

@bot.command()
async def random_anime(ctx):
    """Fetches a random anime."""
    try:
        anime_id = random.randint(1, 10000)
        anime = jikan.anime(anime_id)
        title = anime['title']
        synopsis = anime['synopsis']
        url = anime['url']
        response = f"**{title}**\n{synopsis}\nMore info: {url}"
    except Exception as e:
        response = f"Error: {str(e)}"
    await ctx.send(response)

@bot.command()
async def top_anime(ctx):
    """Fetches top anime list."""
    try:
        top = jikan.top('anime')
        response = "**Top Anime:**\n"
        for anime in top['top'][:10]:
            response += f"{anime['title']} - {anime['url']}\n"
    except Exception as e:
        response = f"Error: {str(e)}"
    await ctx.send(response)

@bot.command()
async def top_manga(ctx):
    """Fetches top manga list."""
    try:
        top = jikan.top('manga')
        response = "**Top Manga:**\n"
        for manga in top['top'][:10]:
            response += f"{manga['title']} - {manga['url']}\n"
    except Exception as e:
        response = f"Error: {str(e)}"
    await ctx.send(response)

@bot.command()
async def season(ctx, year: int, season: str):
    """Fetches anime list by season."""
    try:
        season_list = jikan.season(year, season)
        response = f"**Anime in {season} {year}:**\n"
        for anime in season_list['anime'][:10]:
            response += f"{anime['title']} - {anime['url']}\n"
    except Exception as e:
        response = f"Error: {str(e)}"
    await ctx.send(response)

@bot.command()
async def schedule(ctx, day: str):
    """Fetches anime schedule for a specific day."""
    try:
        schedule = jikan.schedule(day=day)
        response = f"**Anime schedule for {day}:**\n"
        for anime in schedule[day][:10]:
            response += f"{anime['title']} - {anime['url']}\n"
    except Exception as e:
        response = f"Error: {str(e)}"
    await ctx.send(response)

# Run the bot with the token
bot.run('YOUR_DISCORD_BOT_TOKEN')
