import requests

def fetch_planet_data():
    """
    Fetches data about planets from the Solar System OpenData API.
    Returns:
        List of planets, each represented as a dictionary.
    """
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    
    # Extract only planet data
    planet_data = [
        {
            'name': planet['englishName'],
            'mass': planet.get('mass', {}).get('massValue', 'N/A'),
            'orbit_period': planet.get('sideralOrbit', 'N/A')
        }
        for planet in planets if planet['isPlanet']
    ]
    
    return planet_data

def print_planet_data(planets):
    """
    Prints the data of each planet in a user-friendly format.
    """
    for planet in planets:
        name = planet['name']
        mass = planet['mass']
        orbit_period = planet['orbit_period']
        print(f"Planet: {name}, Mass: {mass} kg, Orbit Period: {orbit_period} days")

def find_heaviest_planet(planets):
    """
    Finds the heaviest planet from the list of planets.
    Args:
        planets (list): List of planets where each planet is a dictionary.
    Returns:
        Tuple with the name and mass of the heaviest planet.
    """
    heaviest_planet = max(planets, key=lambda x: float(x['mass']) if x['mass'] != 'N/A' else 0)
    return heaviest_planet['name'], heaviest_planet['mass']

def main():
    planets = fetch_planet_data()
    
    # Print planet data
    print("Planets Data:")
    print_planet_data(planets)
    
    # Find and print the heaviest planet
    name, mass = find_heaviest_planet(planets)
    print(f"\nThe heaviest planet is {name} with a mass of {mass} kg.")

if __name__ == "__main__":
    main()
