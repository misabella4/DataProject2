# Data Project 2 – Weather ChatBot

This is a Flask-based chatbot app that allows users to ask weather-related questions about world capital cities. It combines live weather data from a public API with a local CSV dataset using a Python ETL pipeline.

# Features
- Bot answers questions about the current weather for any world capital city
- Uses weather API (https://open-meteo.com/) to provide the wind speed in that city
- Uses CSV file from Kaggle to generate the ETL script (city, UV index, and temperature in Celsius)

# ETL Pipeline 
- `etl/weather_etl.py`:
  - Extract: Reads external dataset from Kaggle CSV
  - Transform: Cleans the CSV columns, normalizes the city names, and removes duplicates
  - Load: Saves relevant info into a new CSV`before chatbot uses anything

# Flask App
- Routes:
  - `/chat` – main page
  - `/clear` – clears chats
  - `/about` – description
- `/templates/` folder has the HTML code for the appearance of the app

# GCP Instance
The chatbot can be deployed on a Google Cloud VM and is publicly accessible at *[http://34.66.92.177:8080](http://34.66.92.177:8080)*

# Discord
Our chatbot is also connected to Discord using `discord.py`. You can ask the weather questions directly in your server, where the bot processes input using the same logic as it did on Flask. It will respond in the same format as before showing the temperature, UV index, and wind speed for that city.

# Reflection
See the reflection.md tab in our repo
