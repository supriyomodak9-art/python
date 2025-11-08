# Requirements : transformers torch sentencepiece

from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")

print("AI Chatbot (GPT-2)\nType 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Generate response
    result = chatbot(user_input, max_length=60, do_sample=True)[0]['generated_text']

    # Remove the original prompt from output if repeated
    response = result[len(user_input):].strip()
    print("Bot:", response)

