#!/usr/bin/env python

from openai import OpenAI
import os

apikey = os.environ['DEEPSEEK_API_KEY']

openai = OpenAI(
    base_url = "https://api.deepseek.com",
    api_key = apikey
)

prompt = "A giraffe skiing"
model = "janus-pro-7b"
# model="deepseek-chat"


def main() -> None:
    # Generate an image based on the prompt
    response = openai.images.generate(prompt=prompt, model=model)

    # Prints response containing a URL link to image
    print(response)


if __name__ == "__main__":
    main()
