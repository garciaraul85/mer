import openai
client = openai.OpenAI()

reponse = client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Who won the cricket world cup in 2019?"}
    ]
)

print(reponse.choices[0].message.content)