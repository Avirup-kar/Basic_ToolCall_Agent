import tool_groq
import asyncio
import json


async def call_llm():
    resInput = input("Enter your message to get the weather report: ")
    res = await tool_groq.ask_groq(resInput)

    print(res)


asyncio.run(call_llm())