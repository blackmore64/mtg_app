from src.api.mtg_api import fetch_cards
from src.storage.json_storage import save_cards

def main():
    cards = fetch_cards()

    save_cards(cards)

    print(cards[0].keys())
    print(cards[0]["name"])
    print(len(cards))





# This acts as a guard, so the program doesn't run
# Unless it is specifically called to run.
if __name__ == "__main__":
    main()
