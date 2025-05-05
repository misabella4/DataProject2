import discord
from discord.ext import commands
import pandas as pd
import re
import requests

# Load weather data
weather_df = pd.read_csv('data/local_weather.csv')

# Function to fetch wind speed from Open-Meteo API
def get_wind_speed(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=wind_speed_10m"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get('current', {}).get('wind_speed_10m')
    except Exception as e:
        print(f"API error: {e}")
        return None

# Insert your bot token at runtime (keep secrets out of version control)
DISCORD_BOT_TOKEN = input("Enter your Discord bot token: ").strip()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Function to find and respond with weather data
def get_weather_reply(user_message):
    city = None
    user_message_lower = user_message.lower()
    for c in weather_df['city']:
        if re.search(rf'\b{re.escape(c.lower())}\b', user_message_lower):
            city = c
            break
    if city:
        row = weather_df[weather_df['city'].str.lower() == city.lower()].iloc[0]
        temp = row['temp']
        uv = row['uv']
        lat = row['latitude']
        lon = row['longitude']
        wind = get_wind_speed(lat, lon)
        if wind is not None:
            return f"In {city}, it's {temp}°C with a UV index of {uv}. Wind speed: {wind} km/h."
        else:
            return f"In {city}, it's {temp}°C with a UV index of {uv}. Live wind data unavailable."
    else:
        return "Please mention a valid capital city. (Ex: 'What's the weather in Paris?')"

@bot.event
async def on_ready():
    print(f"🌤️ Weather bot logged in as {bot.user}")

@bot.command()
async def weather(ctx, *, question):
    reply = get_weather_reply(question)
    await ctx.send(reply)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("!"):
        await bot.process_commands(message)
    else:
        reply = get_weather_reply(message.content)
        await message.channel.send(reply)

bot.run(DISCORD_BOT_TOKEN)
