import openai
import gradio as gr

client = openai.OpenAI()

def get_open_ai_response(question):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "user", "content": question}]
    )

    return response.choices[0].message.content

# Create user interface for our chatbot
iface = gr.Interface(fn=get_open_ai_response, inputs="text", outputs="text")
iface.launch()