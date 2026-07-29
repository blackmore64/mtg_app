import json


# Function for saving cards to cards.json.
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


# Function for loading cards from cards.json.
def load_cards(filename="data/cards.json"):
    """
    Loads the list of cards from a JSON file.

    Args:
        filename (str): The name of the file
        to load the cards from.

    Returns:
        list: List of card dictionaries.
    """
    with open(filename, "r", encoding = "utf-8") as f:
        return json.load(f)