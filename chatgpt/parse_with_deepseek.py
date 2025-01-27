from openai import OpenAI
import os
from utils import get_historical_weather_data

apikey = os.environ['DEEPSEEK_API_KEY']

results = get_historical_weather_data()
prompt = "Based on the following API results data in json format, parse this data into a readable table of data: " + str(results)

client = OpenAI(
    base_url = "https://api.deepseek.com",
    api_key = apikey
)

messages = []
while True:
    response = client.chat.completions.create(
        # model="Janus-Pro-7B",
        model="deepseek-chat",
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
