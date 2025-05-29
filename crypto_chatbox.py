bot_name = "CryptoBuddy"
bot_tone = "friendly"

def respond(message):
    if bot_tone == "friendly":
        return f"Hey there! {message}"
    elif bot_tone == "professional":
        return f"Greetings. {message}"
    else:
        return message

def add_disclaimer(message):
    return f"{message}\n\n Disclaimer: Crypto is risky—always do your own research!"

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def handle_query(user_query):
    query = user_query.lower()

    if "sustainable" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return add_disclaimer(respond(f"Invest in {recommend}! It’s eco-friendly and has long-term potential!"))

    elif "growth" in query or "long-term" in query or "trending up" in query:
        candidates = [name for name, data in crypto_db.items()
                      if data["price_trend"] == "rising" and data["market_cap"] in ("high", "medium")]
        if candidates:
            return add_disclaimer(respond(f"{candidates[0]} is trending up and looking strong for long-term growth!"))
        else:
            return respond("Hmm, I couldn't find a great match right now.")

    elif "energy" in query:
        low_energy = [name for name, data in crypto_db.items() if data["energy_use"] == "low"]
        if low_energy:
            return respond(f"{low_energy[0]} uses the least energy — a great pick for eco-conscious investors!")

    elif "bitcoin" in query:
        return respond(f"Bitcoin is a powerhouse with a high market cap, but uses a lot of energy and has low sustainability.")

    elif "ethereum" in query:
        return respond(f"Ethereum is stable with a high market cap and medium energy use. Solid choice.")

    else:
        return respond("I'm not sure what you mean. Try asking about 'sustainability', 'growth', or a specific coin like Bitcoin.")

def run_chatbot():
    print(f"{bot_name} : Hello! Ask me about crypto growth, sustainability, or specific coins.")
    print("Type 'exit' to leave the chat.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print(f"{bot_name} : Bye! Remember to do your own research!")
            break
        response = handle_query(user_input)
        print(f"{bot_name} : {response}\n")

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
