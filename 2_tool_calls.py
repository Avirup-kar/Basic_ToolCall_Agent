import tool_groq
import json


def call_llm():
    res = tool_groq.ask_groq("What is the current weather in Bangalore?")

    
    get_weather = tool_groq.get_weather(arguments["city"])

    print(res)


call_llm() 