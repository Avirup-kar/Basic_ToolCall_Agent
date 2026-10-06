import requests
from dotenv import load_dotenv
from pydantic import BaseModel
import json
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def ask_groq(message):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-oss-20b",
        "max_tokens": 200,

        "messages": [
            # {
            #     "role": "system",
            #     "content": (
            #         "you "
            #     )
            # },
            {
                "role": "user",
                "content": message
            }
        ],
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,
        stream=True
    )

    if response.status_code != 200:
        print("Groq API Error:")
        print(response.text)
        return None

    result = response.json()
    
    content = result["choices"][0]["message"]["content"]


    return content



# 1. Define the actual Python function
def get_weather(city: str):
    return {
        "city": city,
        "temperature": 28,
        "unit": "celsius",
        "condition": "sunny"
    }