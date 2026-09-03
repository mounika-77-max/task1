print("Welcome to Simple Chatbot!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How are you?")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot: My name is ChatBot.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")