import requests
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


class Person(BaseModel):
    name: str
    age: int
    city: str


def ask_groq(message):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-oss-20b",
        "max_tokens": 300,

        "messages": [
            {
                "role": "system",
                "content": "Extract the person's information and return it using the provided schema."
            },
            {
                "role": "user",
                "content": message
            }
        ],

        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "person",
                "strict": True,
                "schema": Person.model_json_schema()
            }
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    result = response.json()

    return result["choices"][0]["message"]["content"]