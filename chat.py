from openai  import OpenAI
client= OpenAI(api_key="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",
               
    base_url="https://openrouter.ai/api/v1")





user_r= input("Enter your question:")
response=client.chat.completions.create(
    model="deepseek/deepseek-chat-v3.1:free",
    messages=[
{
    "role": "user",
    "content": user_r
}
]

)




print (response.choices[0].message.content)