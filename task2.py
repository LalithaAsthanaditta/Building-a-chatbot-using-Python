from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train('chatterbot.corpus.english')

# Optionally, you can provide additional training data
# trainer.train([
#     'Hi',
#     'Hey! How's it going?',
#     'Everything is good.',
# ])

# Get a response to a user input
while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break

    response = chatbot.get_response(user_input)
    print('Bot:', response)
