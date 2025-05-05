import pandas as pd
import os

def extract_data(file_path):
    # Loads raw weather data from the CSV file to use in implementation
    df = pd.read_csv(file_path)
    return df


def prepare_data(df):
    df = df[['country', 'location_name', 'latitude', 'longitude', 'temperature_celsius', 'uv_index']].copy()
    df = df.rename(columns={
        'location_name': 'city',
        'temperature_celsius': 'temp',
        'uv_index': 'uv'
    })
    df.dropna(subset=['country', 'city', 'temp', 'uv', 'latitude', 'longitude'], inplace=True)
    # Normalize case
    df['city'] = df['city'].str.title()
    df['country'] = df['country'].str.title()
    # Drop duplicate (country, city) pairs
    df.drop_duplicates(subset=['country', 'city'], keep='first', inplace=True)
    return df

def load_data(df, output_path='data/local_weather.csv'):
    # Save new, cleaned data to a more organized CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

def run():
    file_path = 'data/raw_global_weather.csv'
    df = extract_data(file_path)
    new_df = prepare_data(df)
    load_data(new_df, output_path='data/local_weather.csv')

if __name__ == '__main__':
    run()