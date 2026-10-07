import requests
from dotenv import load_dotenv
import get_weather
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
    
    messages = messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful weather assistant. "
                "Give a natural, concise weather report including the city, "
                "current temperature, wind speed, and a brief useful detail "
                "such as whether the weather is warm, cool, windy, or pleasant."
                "No need any kind of structure normal text not need any kind of symbol as well"
            )
        },
        {
            "role": "user",
            "content": message
        }
    ]

    data = {
        "model": "openai/gpt-oss-20b",
        "max_tokens": 200,
        
        "tools": tools,

        "messages": messages
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
    res = result["choices"][0]["message"]
    
    if "tool_calls" not in res:
        return res["content"]
    
    print("initiating tool call")
    
    tool_call = res["tool_calls"][0]
    function_name = tool_call["function"]["name"]
    function_id = tool_call["id"]
    arguments = json.loads(tool_call["function"]["arguments"])
    
    if function_name == "get_weather":
       get_weather_result = get_weather.call_weather(arguments["city"])
    

    messages.append(res)
    messages.append({
        "role": "tool",
        "tool_call_id": function_id,
        "name": "get_weather",
        "content": json.dumps(get_weather_result)
    })
    
    data["messages"] = messages
    
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

    return result["choices"][0]["message"]["content"]

