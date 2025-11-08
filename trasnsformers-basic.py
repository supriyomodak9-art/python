from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")

print("Type 'exit' to quit\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    response = chatbot(user_input, max_length=50, do_sample=True)[0]['generated_text']
    print("Bot:", response)
