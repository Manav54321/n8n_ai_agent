import gradio as gr
import requests

N8N_WEBHOOK_URL = "http://localhost:5679/webhook/gradio-chat"

def chat_with_n8n(message, history):
    # Send message to n8n webhook
    try:
        response = requests.post(N8N_WEBHOOK_URL, json={"query": message})
        reply = response.json()[0].get("reply", "No response from n8n")

    except Exception as e:
        reply = f"Error: {e}"
    
    # Update chat history
    history.append((message, reply))
    return history, ""

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Type your message")
    clear = gr.Button("Clear")

    msg.submit(chat_with_n8n, [msg, chatbot], [chatbot, msg])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()
