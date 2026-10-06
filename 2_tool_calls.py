import tool_groq
import json


def call_llm():
    res = tool_groq.ask_groq("What is the current weather in Bangalore?")

    tool_call = res["tool_calls"][0]
    function_name = tool_call["function"]["name"]
    arguments = json.loads(tool_call["function"]["arguments"])

    print(function_name)
    print(arguments["city"])
    # print(res)


call_llm() 