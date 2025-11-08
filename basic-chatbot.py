print(" ██████  ██     ██    ███    ████████ ████████   ███████  ████████ ")
print("██    ██ ██     ██   ██ ██      ██    ██     ██ ██     ██    ██    ")
print("██       ██     ██  ██   ██     ██    ██     ██ ██     ██    ██    ")
print("██       █████████ ██     ██    ██    ████████  ██     ██    ██    ")
print("██       ██     ██ █████████    ██    ██     ██ ██     ██    ██    ")
print("██    ██ ██     ██ ██     ██    ██    ██     ██ ██     ██    ██    ")
print(" ██████  ██     ██ ██     ██    ██    ████████   ███████     ██    ")
print("")
print("by Subhadeep Pramanik")


# Step 1: Ask for user's name
name = input("Bot: Hi there! What's your name?\nYou: ")

# Step 2: Greet user personally
print(f"Bot: Nice to meet you, {name}!")

# Step 3: Start the chat loop
while True:
    user = input(f"{name}: ").lower()

    if "bye" in user:
        print(f"Bot: Goodbye, {name}! Have a great day..")
        break
    elif "how are you" in user:
        print("Bot: I’m just a bot, but I’m feeling awesome today..")
    elif "your name" in user:
        print("Bot: I’m ChatCLI, your friendly Python chatbot!")
    elif "help" in user:
        print("Bot: You can ask me things like 'how are you', 'your name', or say 'bye' to exit.")
    elif "thank" in user:
        print(f"Bot: You’re welcome, {name}!")
    else:
        print("Bot: Hmm... I didn’t quite get that. Try asking something else!")

