import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a dictionary of responses
responses = {
    "hello": "Hi! How can I help you today?",
    "hi": "Hello! What's on your mind?",
    "how are you": "I'm doing well, thanks! How about you?",
    "what is your name": "I'm Chatty, your friendly chatbot!",
    "default": "I didn't understand that. Can you please rephrase?"
}

def process_input(user_input):
    # Tokenize the user's input
    tokens = word_tokenize(user_input.lower())

    # Lemmatize the tokens
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]

    # Join the lemmas back into a string
    input_string = " ".join(lemmas)

    # Check if the input matches a response in the dictionary
    for key in responses:
        if key in input_string:
            return responses[key]

    # If no match, return the default response
    return responses["default"]

def chat():
    print("Welcome to the chatbox! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = process_input(user_input)
        print("Chatty: " + response)

if __name__ == "__main__":
    chat()