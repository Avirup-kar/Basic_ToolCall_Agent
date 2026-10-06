import requests
from dotenv import load_dotenv
from pydantic import BaseModel
import json
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

    # Generate schema from Pydantic
    schema = Person.model_json_schema()

    # Groq requires this
    schema["additionalProperties"] = False

    data = {
        "model": "openai/gpt-oss-20b",
        "max_tokens": 300,

        "messages": [
            {
                "role": "system",
                "content": (
                    "Extract the person's name, age and city. "
                    "Return the information according to the provided schema."
                )
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
                "schema": schema
            }
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    if response.status_code != 200:
        print("Groq API Error:")
        print(response.text)
        return None

    result = response.json()
    
    content = result["choices"][0]["message"]["content"]


    return Person.model_validate(json.loads(content))