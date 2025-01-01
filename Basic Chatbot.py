import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data files (only needs to be done once)
nltk.download('punkt')

# Define chatbot responses using patterns
pairs = [
    [
        r"(hi|hello|hey|heya|howdy)",
        ["Hello! How can I assist you today?", "Hi there! How's it going?"]
    ],
    [
        r"what is your name\??",
        ["I am a chatbot created to assist you. What's your name?"]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1! How can I help you today?"]
    ],
    [
        r"how are you\??",
        ["I'm just a bunch of code, so I don't have feelings, but I'm here to help you!"]
    ],
    [
        r"what can you do\??",
        ["I can have a basic conversation with you, answer simple questions, and provide help. Try asking something!"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I can help with that. Could you provide more details?"]
    ],
    [
        r"(.*) (location|city)\??",
        ["I'm virtual, so I exist everywhere! Where are you from?"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "Bye! Hope to chat with you again soon!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase that?", "Interesting! Tell me more."]
    ]
]

# Initialize the chatbot with pairs and reflections
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I am your chatbot. Type 'quit' to end the chat.\n")
    print("You: ", end="")
    while True:
        user_input = input()
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")
        print("You: ", end="")

if __name__ == "__main__":
    start_chat()
