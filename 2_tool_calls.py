import tool_groq
import json


def call_llm():
    resInput = input("Enter your message to get the weather report: ")
    res = tool_groq.ask_groq(resInput)

    print(res)


call_llm() 