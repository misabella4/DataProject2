# This will be the ChatBot code in Python
from flask import Flask, render_template, request, session, redirect, url_for
import pandas as pd
import requests
import re

app = Flask(__name__)
app.secret_key = "your-secret-key"  # Required for session support

# Weather dataset
weather_df = pd.read_csv('data/local_weather.csv')

# Bot reply cleaner (from Prof Williamson, but modified)
def extract_first_answer(text):
    text = text.strip()
    text = re.sub(r'\b(Bot|Assistant)\s*:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^(OUTPUT|Answer)\s*:\s*', '', text, flags=re.IGNORECASE)
    # Extract new tag content
    for tag in ['RESULT', 'INST', 'ANS']:
        match = re.search(rf'\[{tag}\](.*?)\[/\s*{tag}\]', text, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
    # Clean up
    text = re.sub(r'#?\*\[.*?\]', '', text)
    # Fallback: first sentence or line
    sentence = re.split(r'[.!?]', text)[0]
    return sentence.strip()

# API Call Function
def get_wind_speed(lat, long):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=wind_speed_10m"
    try:
        response = requests.get(url)
        data = response.json()
        wind_speed = data.get('current', {}).get('wind_speed_10m')
        return wind_speed
    except Exception as e:
        print(f"Error getting data from API: {e}")
        return None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return "This is a weather Flask app."

@app.route('/debug')
def debug():
    return "This is the debug route. Everything's (hopefully) fine."

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'history' not in session:
        session['history'] = []
    if request.method == 'POST':
        user_message = request.form['message']
        city = None
        for c in weather_df['city']:
            if c.lower() in user_message.lower():
                city = c
                break
        if city:
            match = weather_df[weather_df['city'].str.lower() == city.lower()]
            if not match.empty:
                row = match.iloc[0]
                temperature = row['temp']
                uv_index = row['uv']
                latitude = row['latitude']
                longitude = row['longitude']
                wind = get_wind_speed(latitude, longitude)
                if wind is not None:
                    bot_reply = (
                        f"In {city}, the local temperature is {temperature}°C with a UV index of {uv_index}. "
                        f"In addition, the current wind speed is {wind} km/h."
                    )
                else:
                    bot_reply = (
                        f"In {city}, the local temperature is {temperature}°C with a UV index of {uv_index}. "
                        "However, I couldn't retrieve live wind data."
                    )
            else:
                bot_reply = f"I could not pull any weather data. Double check your spelling and retry."
        else:
            bot_reply = f"Make sure your city choice is a world capital. Or double check your spelling and retry."
        session['history'].append({'user': user_message, 'bot': bot_reply})
        session.modified = True
    return render_template('chat.html', history=session.get('history', []))

@app.route('/clear', methods=['GET', 'POST'])
def clear():
    session.pop('history', None)
    return redirect(url_for('chat'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)