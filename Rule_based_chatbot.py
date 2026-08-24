import random

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

def recommend():
    choice = input("Beaches, mountains, or cities? ").lower()

    if choice in destinations:
        place = random.choice(destinations[choice])
        print("How about", place, "?")

        answer = input("Do you like it? (yes/no): ").lower()

        if answer == "yes":
            print("Awesome! Enjoy", place, "!")
        else:
            print("Let's try another.")
            recommend()
    else:
        print("Sorry, I don't have that option.")
        recommend()

def packing():
    location = input("Where to? ")
    days = input("How many days? ")

    print(f"Packing tips for {days} days in {location}:")
    print("- Pack comfortable clothes.")
    print("- Bring chargers.")
    print("- Check the weather.")

def joke():
    print(random.choice(jokes))

def help_menu():
    print("\nI can:")
    print("- recommend a place")
    print("- give packing tips")
    print("- tell a joke")
    print("Type 'exit' to stop.\n")

def chat():
    print("Hello! I'm TravelBot.")
    name = input("Your name? ")
    print("Nice to meet you,", name)

    help_menu()

    while True:
        user = input(name + ": ").lower()

        if "recommend" in user or "suggest" in user:
            recommend()
        elif "pack" in user:
            packing()
        elif "joke" in user or "funny" in user:
            joke()
        elif "help" in user:
            help_menu()
        elif "exit" in user or "bye" in user:
            print("Safe travels! Goodbye!")
            break
        else:
            print("Could you rephrase?")

chat()