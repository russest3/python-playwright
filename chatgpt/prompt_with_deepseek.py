from openai import OpenAI
import os
from utils import get_historical_weather_data
import requests

apikey = os.environ['DEEPSEEK_API_KEY']

def get_historical_weather_data():
    response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m')
    return response.text

results = get_historical_weather_data()
prompt = "Based on the following API results data in json format, parse this data into a readable table of data: " + str(results)

client = OpenAI(
    base_url = "https://api.deepseek.com",
    api_key = apikey
)

messages = []
while True:
    response = client.chat.completions.create(
        model="Janus-Pro-7B",
        # model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    if prompt == "quit":
        break
    messages.append(
    {
        'role':'user',
        'content': prompt
    })

print(response.choices[0].message.content)
