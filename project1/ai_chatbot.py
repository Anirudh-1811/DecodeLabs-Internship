import sys
def start_bot():
    bot_responses = {
        "hello": "Greetings! Glad to chat with you today.",
        "hi": "Hello there! How can I help you?",
        "hey": "Hey! Up for a quick chat?",
        "help": "Facts, quotes, system status, or something else? Just ask!",
        "status": "System status is nominal. Logic gates are fully functional.",
        "fact": "Here's a fact: Ketchup was originally sold as a medicine in the 1830s.",
        "quote": "Here's a quote: 'Life is like riding a bicycle. To keep your balance, you must keep moving.' - Albert Einstein",
        "about": "I am a simple rule-based chatbot created for demonstration purposes. I can respond to specific keywords with predefined answers.",
        "weather": "I just know about 'cloud' computing, not the actual weather outside!",
        "blueprint": "The backend architecture relies entirely on the structural Input-Process-Output (IPO) model.",
        "credits": "Powered by Anirudh, co-powered by DecodeLabs!"
    }
    quit_words = {"exit", "bye", "quit", "goodbye"}
    
    print("Chatbot: Hello! I am a rule-based AI assistant. How can I help you today?")
    while True:
        try:
            user_text = input("User: ")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Session interrupted. Goodbye!")
            sys.exit(0)
        text_clean = user_text.strip().lower()
        if not text_clean:
            continue
        if text_clean in quit_words:
            print("Chatbot: Goodbye! Have a great day ahead.")
            break
        default_reply = "I'm sorry, I am a basic rule-based bot and don't understand that command yet."
        answer = bot_responses.get(text_clean, default_reply)
        
        print(f"Chatbot: {answer}")

if __name__ == "__main__":
    start_bot()
