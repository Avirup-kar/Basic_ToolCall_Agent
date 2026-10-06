import tool_groq
import json


def call_llm():
    res = tool_groq.ask_groq("What is the current weather in Bangalore?")

    print(res)


call_llm() 