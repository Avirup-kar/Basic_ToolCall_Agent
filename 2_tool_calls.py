import tool_groq
import json


def call_llm():
    res = tool_groq.ask_groq("What is the current weather in Bangalore?")

    
    get_weather = tool_groq.get_weather(arguments["city"])

    # print(function_name)
    # print(arguments["city"])
    # print(function_id)
    # print(res)
    print(get_weather)


call_llm() 