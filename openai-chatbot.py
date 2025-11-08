# Requirements : pip install openai , openai api key from platform.openai.com

from openai import OpenAI

client = OpenAI(api_key="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")

print(" ChatGPT CLI Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    bot_reply = response.choices[0].message.content
    print("Bot:", bot_reply)

