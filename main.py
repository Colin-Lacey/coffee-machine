MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 100,
    "milk": 3,
    "coffee": 5,
}


def print_resources():
    for entry in resources:
        if entry == "money":
            print("$", end="")
        print(f"{entry}: {resources[entry]}", end="")
        if entry == "water" or entry == "milk":
            print("ml")
        elif entry == "coffee":
            print("g")


# Returns a list of any resources which are insufficient for the requested drink
def get_insufficient_resources(drink: str) -> list:
    sufficient_resources = []
    drink_ingredients = MENU[user_choice]['ingredients']
    for entry in drink_ingredients:
        if resources[entry] < drink_ingredients[entry]:
            sufficient_resources.append(entry)
    return sufficient_resources


operating = True


def make_drink(user_choice):
    pass


def process_coins(user_choice):
    pass


def print_insufficient_resources(drink: str, resources_in_deficit: list):
    print(f"Sorry! there is not enough ", end="")
    for i in range(len(resources_in_deficit)):
        # Difference between the required ingredients for a given drink (in MENU) and ingredients on hand (in resources)
        deficit = MENU[drink]['ingredients'][resources_in_deficit[i]] - resources[resources_in_deficit[i]]
        # When listing things in English, we say "1, 2..., or x"
        # 1
        if i == 0:
            # 1 is the first element, which is simply itself with no preceding punctuation:
            print(f"{resources_in_deficit[i]} (needs {deficit}", end="")
        # 3
        elif i == len(resources_in_deficit) - 1:
            # x is the last element, which is preceded by ", or " and is unique at the end of the list:
            print(f", or {resources_in_deficit[i]} (needs {deficit}", end="")
        # 2
        else:
            # 2... are any other elements, which are preceded only by ", ":
            print(f", {resources_in_deficit[i]} (needs {deficit}", end="")
        # Since "for in range()" will take us through the list in order, this if block will
        # construct a grammatically correct sentence consisting of each insufficient resource
        print(f"{'g' if resources_in_deficit[i] == 'coffee' else 'ml'} more)", end="")
    print(f" for a {drink}.")


# Main loop to operate the machine
while operating:
    user_choice = input("What would you like? (espresso, latte, cappuccino)\n").lower()
    if user_choice == 'report':
        print_resources()
    elif user_choice == 'off':
        # "off" -> stop the program
        operating = False
        break
    elif user_choice == 'latte' or user_choice == 'cappuccino' or user_choice == 'espresso':
        insufficient_resources = get_insufficient_resources(user_choice)
        # Check if there are no insufficient resources
        if len(insufficient_resources) == 0:
            process_coins(user_choice)
            # TODO: Process the coins and determine if they are sufficient
            # TODO: If the coins are sufficient, make the drink and subtract used resources
            # TODO: If the coins are insufficient, inform the user and void the transaction
        else:
            print_insufficient_resources(user_choice, insufficient_resources)




