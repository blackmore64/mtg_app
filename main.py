from src.api.mtg_api import fetch_cards
from src.storage.json_storage import save_cards, load_cards

def main():
    cards = fetch_cards()

    save_cards(cards)

    loaded_cards = load_cards(filename="data/cards.json")

    print(f"Loaded {len(loaded_cards)} cards from data/cards.json")

    print("First Card:")
    print(f"Name: {loaded_cards[0]['name']}")
    print(f"Colors: {loaded_cards[0]['colors']}")
    print(f"Converted Mana Cost: {loaded_cards[0]['cmc']}")
    print(f"Power: {loaded_cards[0]['power']}")
    print(f"Toughness: {loaded_cards[0]['toughness']}")
    if 'supertypes'in loaded_cards[0]:
        print(f"Supertypes: {loaded_cards[0]['supertypes']}")
    else:
        print("Supertypes: None")
    print(f"Subtypes: {loaded_cards[0]['subtypes']}")
    print(f"Types: {loaded_cards[0]['types']}")
    #print(f"Game Format: {loaded_cards[0]['gameFormat']}")
    print(f"Set: {loaded_cards[0]['set']}")
    print("Legalities:")
    """
    So, for this next step, we're dealing with the
    'legalities' dictionary, which looks like this:
    {'format': 'Commander', 'legality': 'legal'}

    So, we're going to be using a FOR loop to iterate
    through the various play formats and print them,
    along with their corresponding legality status.
    """
    for legality in loaded_cards[0]['legalities']:
        print(f"{legality['format']}: {legality['legality']}")


    





# This acts as a guard, so the program doesn't run
# Unless it is specifically called to run.
if __name__ == "__main__":
    main()
