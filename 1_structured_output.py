import structured_groq


def call_llm():
   res = structured_groq.ask_groq("Give me the name, age and city of a fictional person.")
    
   print(res)
   print(res.name)
   print(res.age)
   print(res.city)
   
   
call_llm() 