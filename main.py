from src.api.mtg_api import fetch_cards
from src.storage.json_storage import save_cards, load_cards


# Cleaning up the function name to be more specific.
# (search_cards_by_format() vs. search_cards()).
def search_cards_by_format(cards, play_format):

        """
        Here, I've made a user-input function,
        which will return the names of any
        cards in the JSON which are legal in a given
        play format.

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
    
    # Adding .title() here, to allow for lower-case input.
    search = input("Please enter a play format to search "
    "for legal cards: ").title()

    if search not in ["Standard", "Modern", "Legacy", "Vintage", "Commander"]:
        print("Invalid input. Please enter a valid play format.")
        return
    results = search_cards_by_format(loaded_cards, search)

    print(f"Found {len(results)} cards legal in {search}.")

    """
    I was noticing some duplicates in the card name
    results, so I decided to add a multiverse ID to
    the results, as well.  As I suspected, some cards
    have double-printings (foil versions, etc.), and
    as a result, have no multiverse ID.
    """
    # Some card variants (foils, etc.) don't have
    # a multiverse ID, so I'm using .get() here
    # to check for an ID, and return no value if none
    # exists.
    for card in results:
        multiverse_id = card.get("multiverseid")
        print(f"{card['name']}, {multiverse_id}")

# This acts as a guard, so the program doesn't run
# Unless it is specifically called to run.
if __name__ == "__main__":
    main()
