import json, requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"  # Count, next, previous, results
pokemon_dict = {}


def getting_pokemon_dictionary(URL: str):
    next_url = URL
    while next_url is not None:
        response = requests.get(next_url)
        data = response.json()
        for result in data["results"]:
            pokemon_id = int(result["url"].split("/")[-2])
            pokemon_dict[pokemon_id] = {"name": result["name"],
                                                       "url": result["url"]}
        next_url = data["next"]
        print(next_url)


getting_pokemon_dictionary(BASE_URL)
