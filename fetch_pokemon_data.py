import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return data

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon_name in pokemon_list:
        data = fetch_pokemon_data(pokemon_name)
        total_weight += data['weight']
    return total_weight / len(pokemon_list)

def main():
    pokemon_names = ["pikachu", "bulbasaur", "charmander"]
    
    for pokemon_name in pokemon_names:
        data = fetch_pokemon_data(pokemon_name)
        name = data['name']
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        print(f"Name: {name}")
        print(f"Abilities: {', '.join(abilities)}")
    
    average_weight = calculate_average_weight(pokemon_names)
    print(f"Average Weight: {average_weight:.2f}")

if __name__ == "__main__":
    main()
