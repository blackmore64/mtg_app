from src.api.mtg_api import fetch_cards
from src.storage.json_storage import save_cards, load_cards


"""
Creating the beginnings of a basic search function
here, which will begin looking for various legalities
for various formats.  As I continue, this is going to
become more robust, and will eventually rely on user
input, rather than these static testing values.
"""
def search_cards(play_format):
        cards = load_cards(filename="data/cards.json")

        """
        Here, I'm creating the beginnings of a search
        function, which will return the names of any
        cards in the JSON which are legal in a given
        play format.  This will be changed later to
        accept user input, making it more dynamic.

        Currently, it's using "any" to create a boolean
        search, which will return True for a given card
        if both the specified play format and
        legality (in this case, "Legal") match.
        If this is the case, the card will then be
        added to the results list, which will be
        returned at the end of the function.
        """

        results = [
             item
             for item in cards
             if any(
                  legality.get("format") == play_format
                    and legality.get("legality") == "Legal"
                    for legality in item.get("legalities", [])
             )
        ]

        return results


def main():

    """
    Temporarily commenting out both the fetch_cards()
    and also the save_cards() functions;  recently,
    the API was down (returning a 503 error), so I
    decided just to temporarily skip updating them, and
    for now simply focus on working with the data from
    the already-created JSON file (which is the main
    focus at the moment, anyway).
    """
    #cards = fetch_cards()

    #save_cards(cards)

    loaded_cards = load_cards(filename="data/cards.json")

    # Also commenting out this section temporarily,
    # As I currently just want the results from the
    # Newly-created search function to return.
    """
    # Creating a variable here, for shortening purposes.
    cards = loaded_cards

    print(f"Loaded {len(loaded_cards)} cards from data/cards.json")
    
    print("First Card:")
    print(f"Name: {cards[0]['name']}")
    print(f"Colors: {cards[0]['colors']}")
    print(f"Converted Mana Cost: {cards[0]['cmc']}")
    print(f"Power: {cards[0]['power']}")
    print(f"Toughness: {cards[0]['toughness']}")
    if 'supertypes'in cards[0]:
        print(f"Supertypes: {cards[0]['supertypes']}")
    else:
        print("Supertypes: None")
    print(f"Subtypes: {cards[0]['subtypes']}")
    print(f"Types: {cards[0]['types']}")
    print(f"Set: {cards[0]['set']}")
    print("Legalities:")
    
    So, for this next step, we're dealing with the
    'legalities' dictionary, which looks like this:
    {'format': 'Commander', 'legality': 'legal'}

    So, we're going to be using a FOR loop to iterate
    through the various play formats and print them,
    along with their corresponding legality status.
    
    for legality in cards[0]['legalities']:
        print(f"{legality['format']}: {legality['legality']}")
    """
    results = search_cards("Commander")

    print(f"Found {len(results)} cards legal in Commander.")

    for card in results:
        print(card["name"])

# This acts as a guard, so the program doesn't run
# Unless it is specifically called to run.
if __name__ == "__main__":
    main()
