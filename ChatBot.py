# Youtube_Tutorial_url = "https://youtu.be/hyY2RKb-qnM?si=8mmMwSK0HwRrEypG"

# First you will need to install the following libraries:
# pip install groq or py -m pip install groq

# Getting Api Key from Groq
# 1. Go to https://console.groq.com/home
# 2. Create an account or log in if you already have one.
# 3. Once logged in, navigate to the API Keys section.
# 4. Click on "Create API Key" or a similar button to generate a new API key.
# 5. Enter Display name and select no expiration date for the key.
# 6. Copy the generated API key and keep it secure, as you'll need it to access Groq's services.

# Code

from groq import Groq

Client = Groq(api_key="Here") # Paste your API key here

print("Welcome to the Chat Bot! Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Exiting the chat bot. Goodbye!")
        break
    
    print("Chat Bot: ",end="", flush=True)

    stream = Client.chat.completions.create(
        model="llama-3.1-8b-instant",  # You can change the model to any other available model in Groq's API
        messages=[
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": user_input}
        ],
        stream=True  #Enable streaming to get partial responses as they are generated
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

    print()  # Print a newline after the bot's response