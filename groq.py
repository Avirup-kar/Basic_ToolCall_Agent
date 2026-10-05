import requests
from dotenv import load_dotenv
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
        "messages": [
            {
                "role": "system",
                "content": "You are Avirup, a helpful message assistant. Give a relevent message answers based on previous message data. And the messag is bengali but writeen in english Alphabet like this {Ami valo achi}.Be clear and direct. Avoid unnecessary details, long explanations, and repetition. Respond naturally for spoken conversation, if the messag incuse funny thing then you cand do that as well"
            },
            {
                "role": "user",
                "content": message
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    return result["choices"][0]["message"]["content"]