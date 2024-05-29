#pip install telepot

lyrics = "We're no strangers to love You know the rules and so do I (Do I) A full commitment's what I'm thinking of You wouldn't get this from any other guy"

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why was the math book sad? Because it had too many problems.",
    "What do you get if you cross a snowman and a vampire? Frostbite.",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call a dinosaur with an extensive vocabulary? A thesaurus.",
    "Why can't you give Elsa a balloon? Because she will let it go.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why was the computer cold? It left its Windows open!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "What do you get when you cross a fish and an elephant? Swimming trunks.",
    "Why was the math book sad? It had too many problems.",
    "Why do seagulls fly over the sea? Because if they flew over the bay, they'd be bagels."
]

import random
import telepot
from time import sleep

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == '/start':
        myAwesomeBot.sendMessage(chat_id, "Hello I am your silly bot!")

    elif command == '/help':
        myAwesomeBot.sendMessage(chat_id, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    elif command == '/silly':
        myAwesomeBot.sendMessage(chat_id, lyrics)

    elif command == '/joke':
        myAwesomeBot.sendMessage(chat_id, random.choice(jokes))

    elif command == '/roll':
        myAwesomeBot.sendMessage(chat_id, str(random.randint(1,6)))

    elif command == '/hello':
        myAwesomeBot.sendMessage(chat_id, 'Hello!')

    elif command == '/bye':
        myAwesomeBot.sendMessage(chat_id, 'Bye!')

myAwesomeBot = telepot.Bot('7098495536:AAESDMoTohK1luhElrGy_guTgT29DFdE1A4')
myAwesomeBot.message_loop({'chat':action})

while True:
    sleep(1)