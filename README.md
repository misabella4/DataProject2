# Data Project 2 – Weather ChatBot

This is a Flask-based chatbot app that allows users to ask weather-related questions about world capital cities. It combines live weather data from a public API with a local CSV dataset using a Python ETL pipeline.

## Features
- Bot responds to weather questions for any world capital
- Uses weather API (https://open-meteo.com/) to provide the live wind speed in that city
- Uses CSV file from Kaggle to generate the ETL script (city name, UV index, and temperate in Celsius)

## ETL Pipeline
- `etl/weather_etl.py`:
  - Extract: Reads external dataset from Kaggle CSV
  - Transform: Cleans the CSV columns, normalizes the city names, and removes duplicates
  - Load: Saves relevant info into a new CSV`before chatbot uses anything

## Flask App
- Routes:
  - `/chat` – main chat interface
  - `/clear` – resets session and clears chats
  - `/about` – mini app description
- `/templates/` folder contains more visual code for the appearance of the app

## GCP Instance
The chatbot can be deployed on a Google Cloud VM! It is publicly accessible at: *[http://34.66.92.177:8080](http://34.66.92.177:8080)*

# BONUS - Discord Integration
Our chatbot is also connected to Discord using `discord.py`. You can ask weather questions directly in a Discord server. The bot processes input using the same logic as it did on Flask and can respond in the same format with temperature, UV index, and live wind speed data.

## Reflection
See the reflection.md tab in GitHub repo!
