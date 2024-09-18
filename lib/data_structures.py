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
    return [spicy_food['name'] for spicy_food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return filter(lambda spicy_food: spicy_food['heat_level'] > 5, spicy_foods)

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        name = spicy_food['name']
        cuisine = spicy_food['cuisine']
        heat_level = spicy_food['heat_level']
        heat_level_emoji = '🌶' * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food['cuisine'] == cuisine:
            return spicy_food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
        

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for spicy_food in spicy_foods:
        total_heat_level += spicy_food['heat_level']
    num_of_spicy_foods = len(spicy_foods)
    return total_heat_level / num_of_spicy_foods

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods