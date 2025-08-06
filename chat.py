import requests

N8N_WEBHOOK_URL = "http://localhost:5679/webhook/gradio-chat"

def chat():
    print("Chat with your n8n AI Agent! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Send user message to n8n
        try:
            response = requests.post(N8N_WEBHOOK_URL, json={"query": user_input})
            data = response.json()

            # Handle list or object response
            if isinstance(data, list):
                # reply = data[0].get("reply", "No response from n8n")
                reply = data[0].get("reply", "No response from n8n")
            else:
                reply = data.get("reply", "No response from n8n")

        except Exception as e:
            reply = f"Error: {e}"

        print(f"Agent: {reply}\n")

if __name__ == "__main__":
    chat()
