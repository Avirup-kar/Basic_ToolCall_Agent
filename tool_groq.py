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
    
#2. Describe the function to the model (the tool definition)    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get current weather for a location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "The city to get weather for"
                        },
                    },
                    "required": ["city"]
                }
            }
        }
    ]

    data = {
        "model": "openai/gpt-oss-20b",
        "max_tokens": 200,
        
        "tools": tools,

        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a weather assistant. Respond to the user question and use tools if needed to answer the query."
                )
            },
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
    
    # content = result["choices"][0]["message"]["content"]


    return result["choices"][0]["message"]



# 1. Define the actual Python function
def get_weather(city: str):
    return {
        "city": city,
        "temperature": 28,
        "unit": "celsius",
        "condition": "sunny"
    }