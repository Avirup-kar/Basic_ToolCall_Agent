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

        # Maximum number of tokens the model can generate
        "max_tokens": 300,

        "messages": [
            {
                "role": "system",
                "content": (
                    "You are Avirup, a helpful message assistant. "
                    "Give relevant message answers based on previous message data. "
                    "The message is Bengali but written in English alphabet like "
                    "this {Ami valo achi}. "
                    "Be clear and direct. Avoid unnecessary details, long "
                    "explanations, and repetition. Respond naturally for spoken "
                    "conversation. If the message includes something funny, "
                    "you can be funny as well."
                )
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