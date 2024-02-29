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
    names = []
    for food in spicy_foods:
        name = food['name']
        names.append(name)

    return names
print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
    foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            foods.append(food)
    return foods

print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        heat_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    
    print_spicy_foods(spiciest_foods)
print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods == 0:
        return 0
    return total_heat / num_foods


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
new_spicy_food = {
    "name": "Griot",
    "cuisine": "Haitian",
    "heat_level": 10,
}
updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
print(updated_spicy_foods)