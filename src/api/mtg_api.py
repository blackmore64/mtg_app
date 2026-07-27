import requests

url = "https://api.magicthegathering.io/v1/cards"


def fetch_cards():

    response = requests.get(url)

    # Raise an exception for HTTP errors
    response.raise_for_status()

    data = response.json()

    return data.get("cards", [])

