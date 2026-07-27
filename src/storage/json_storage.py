import json

def save_cards(cards, filename="data/cards.json"):
    """
    Saves the list of cards to a JSON file.

    Args:
        cards (list): List of card dictionaries.
        filename (str): The name of the file to 
        save the cards to.
    """
    with open(filename, "w", encoding = "utf-8") as f:
        json.dump(cards, f, indent = 4)