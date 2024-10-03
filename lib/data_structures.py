spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # Extract names of spicy foods
    names = [food['name'] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    # Return a list of foods where the spiciness level is greater than 5
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food['heat_level']  # Repeat 🌶 based on the spiciness level
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Filter spicy foods by cuisine and return the first match
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None  # In case no match is found

def print_spiciest_foods(spicy_foods):
# Filter spicy foods where spiciness (heat level) is greater than 5
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    # Print each food in the required format
    for food in spiciest_foods:
        heat_level_emojis = "🌶" * food['heat_level']  # Repeat 🌶 based on the spiciness level
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")


def get_average_heat_level(spicy_foods):
     # Calculate the total heat level using the correct key 'heat_level'
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    
    # Calculate the average by dividing the total by the number of spicy foods
    average_heat_level = total_heat_level / len(spicy_foods) if spicy_foods else 0
    
    return average_heat_level  # Make sure to return the result

def create_spicy_food(spicy_foods, spicy_food):
    # Add the new spicy food to the list
    spicy_foods.append(spicy_food)
    
    # Return the updated list of spicy foods
    return spicy_foods