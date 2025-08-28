#Program: 
import nltk 
from nltk.chat.util import Chat, reflections 
from datetime import datetime 
 
nltk.download('punkt') 
 
# Define the patterns and responses for the chatbot 
chatbot_responses = [ 
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']), 
    (r'how are you?', ['I am doing well, thank you!', 'I am just a computer program, but I am functioning 
properly.']), 
    (r'what is your name?', ['I am a chatbot. You can call me ChatGPT!', 'I am known as ChatGPT.']), 
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']), 
    (r'favorite color', ['I don\'t have a favorite color, but I can talk about colors! What\'s your favorite 
color?']), 
    (r'my favorite color is (.*)', ['That\'s a nice color! Mine is virtual, so I don\'t have one.']), 
    (r'favorite destination', ['I haven\'t been to any destination, but I can help you find information about 
great places! Any specific destination in mind?']), 
    (r'my favorite destination is (.*)', ['That sounds like a wonderful destination!']), 
    (r'weather', ['I do not have real-time information. You can check a reliable weather website or app 
for the current weather.']), 
    (r'current time', ['The current time is {}'.format(datetime.now().strftime("%H:%M"))]), 
    (r'(.*)', ['I am sorry, I didn\'t quite understand that.']), 
] 
 
# Create the chatbot using the Chat class 
chatbot = Chat(chatbot_responses, reflections) 
 
def run_chatbot(): 
    print("Chatbot: Hi! How can I help you today? (Type 'bye' to exit)") 
    while True: 
        user_input = input("You: ") 
        if user_input.lower() == 'bye': 
            print("Chatbot: Goodbye!") 
            break 
        else: 
            response = chatbot.respond(user_input) 
            print("Chatbot:", response) 
 
run_chatbot() 
 
'''
Output: 
 
Chatbot: Hi! How can I help you today? (Type 'bye' to exit) 
You: hello 
Chatbot: Hello! 
You: how are you? 
Chatbot: I am doing well, thank you! 
You: what is your name? 
Chatbot: I am a chatbot. You can call me ChatGPT! 
You: current time 
Chatbot: The current time is 21:31
'''