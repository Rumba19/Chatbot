from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('TestBot')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Start conversation
print("Start chatting with TerminalBot (type 'exit' to stop):")
while True:
    user_input = input("user: ")
    if user_input.lower() == 'exit':
        print("bot: Goodbye!")
        break
    response = bot.get_response(user_input)
    print(f"bot: {response}")
