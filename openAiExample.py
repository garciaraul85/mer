import openai
client = openai.OpenAI()

reponse = client.chat.completions.create(
    model= "gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": "Provide a JSON response with the following structure: {'winner': 'string', 'event': 'string', 'year': 'number', 'runner_up': 'string', 'number_of_titles': 'number', 'final_location': 'string'} for any sports event inquiries."},
        {"role": "user", "content": "Who won the cricket world cup in 2015?"}
    ],
    #seed=1 # set the same response
    response_format={"type": "json_object"}
)

print(reponse.choices[0].message.content)