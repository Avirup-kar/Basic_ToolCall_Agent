import tool_groq


def call_llm():
   res = tool_groq.ask_groq("What is the current weather in Bangalore?")
    
   print(res)
   
   
call_llm() 