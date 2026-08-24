import colorama
from colorama import Fore
from textblob import TextBlob

colorama.init()

print(Fore.CYAN + "Welcome to Sentiment Spy!")

name = input("Enter your name: ")

print("Hello", name)
print("Enter a sentence to check its sentiment.")
print("Type 'exit' to stop.\n")

history = []

while True:
    text = input(">> ")

    if text.lower() == "exit":
        print("Goodbye!")
        break

    if text.lower() == "history":
        for item in history:
            print(item)
        continue

    if text.lower() == "reset":
        history.clear()
        print("History cleared!")
        continue

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.25:
        sentiment = "Positive"
        print(Fore.GREEN + "Positive 😊")

    elif polarity < -0.25:
        sentiment = "Negative"
        print(Fore.RED + "Negative 😞")

    else:
        sentiment = "Neutral"
        print(Fore.YELLOW + "Neutral 😐")

    print("Polarity:", round(polarity, 2))

    history.append((text, sentiment, round(polarity, 2)))