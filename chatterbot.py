# Requirements : pip install chatterbot==1.0.5 chatterbot-corpus


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("LocalBot")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

print("Local Chatbot (type 'exit' to quit)\n")
while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break
    reply = bot.get_response(msg)
    print("Bot:", reply)

