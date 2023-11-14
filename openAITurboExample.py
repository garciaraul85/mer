import openai
client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[{"role": "user", "content": "Who won the cricket world cup in 2019?"}]
)

print(response.choices[0].message.content)