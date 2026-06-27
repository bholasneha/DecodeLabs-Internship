# ====================================
# Rule-Based Chatbot in Python
# ====================================

print("🤖 Simple Rule-Based Chatbot")
print("Type 'bye' to exit.\n")

while True:

    # Take user input
    user_input = input("You: ").lower().strip()

    # Greeting Rules
    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How are you?")

    # Asking Name
    elif user_input == "what is your name":
        print("Bot: My name is ChatBot.")

    # Asking About Python
    elif user_input == "what is python":
        print("Bot: Python is a programming language.")

    # Asking Time
    elif user_input == "time":
        print("Bot: I cannot show real time now.")

    # Goodbye Rule
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    # Default Response
    else:
        print("Bot: Sorry, I don't understand.")