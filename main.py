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

profit = 0
resources = {
    "water": 300,
    "milk": 300,
    "coffee": 500,
}


def print_report():
    print(f"Money: ${profit}")
    for entry in resources:
        print(f"{entry}: {resources[entry]}", end="")
        if entry == "water" or entry == "milk":
            print("ml")
        elif entry == "coffee":
            print("g")


# Returns a list of any resources which are insufficient for the requested drink
def get_insufficient_resources(drink: str) -> list:
    insufficient_resources = []
    drink_ingredients = MENU[user_choice]['ingredients']
    for entry in drink_ingredients:
        if resources[entry] < drink_ingredients[entry]:
            insufficient_resources.append(entry)
    return insufficient_resources


operating = True


def make_drink(drink: str):
    # Loop through each ingredient and subtract its required amount from our total resources
    for entry in MENU[user_choice]['ingredients']:
        resources[entry] -= MENU[user_choice]['ingredients'][entry]
    print(f"Here is your {drink}!")
    if drink == 'latte':
        print('☕🍶')
    elif drink == 'cappuccino':
        print('☕')
    elif drink == 'espresso':
        print('☕☕')
    print("Enjoy!\n")


def process_coins(user_choice: str) -> bool:
    user_choice_price = MENU[user_choice]['cost']
    balance = user_choice_price
    str_balance = '${:,.2f}'.format(balance)
    print(f"A {user_choice} costs {str_balance}. Please insert equivalent coins now "
          f"(enter 'penny', 'nickel', 'dime', 'quarter', 'loonie', or 'toonie' one by one) or enter 'c' to cancel.")
    paid = False
    while not paid:
        str_balance = '${:,.2f}'.format(balance)
        coin = input(f'{str(str_balance)} is the remaining balance.\n').lower()
        if coin == 'c':
            str_change = ' Returning already submitted money totalling ${:,.2f}.'.format(user_choice_price - balance) \
                if user_choice_price - balance >= 0.01 else ''
            print(f"Cancelling order. {str_change}")
            break
        elif coin.isalpha():
            if coin == 'penny':
                balance -= 0.01
            elif coin == 'nickel':
                balance -= 0.05
            elif coin == 'dime':
                balance -= 0.10
            elif coin == 'quarter':
                balance -= 0.25
            elif coin == 'loonie' or coin == 'one':
                balance -= 1
            elif coin == 'toonie' or coin == 'two':
                balance -= 2
            else:
                print(f"I'm sorry, '{coin}' doesn't appear to be a valid entry.")
                continue
            print(f"{coin.title()} accepted. ", end="")
        else:
            print("I'm sorry, that doesn't appear to be a valid entry.")
        if balance < 0.01:
            paid = True
            str_change = f' Your change is {"${:,.2f}".format(abs(balance))}.' if abs(balance) > 0.01 else ""
            print(f"\nBalance paid in full.{str_change} Drink will now be dispensed.")
            return True
    return False


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
        print_report()
    elif user_choice == 'off':
        # input "off" -> stop the program
        operating = False
        break
    elif user_choice == 'latte' or user_choice == 'cappuccino' or user_choice == 'espresso':
        insufficient_resources = get_insufficient_resources(user_choice)
        # Check if there are no insufficient resources
        if len(insufficient_resources) == 0:
            # process_coins will loop through asking user to submit enough coins for the drink
            drink_paid = process_coins(user_choice)
            if drink_paid:
                profit = MENU[user_choice]['cost']
                make_drink(user_choice)
            else:
                print(f"{user_choice.title()} purchase was unsuccessful. Returning to drink menu.")
        else:
            print_insufficient_resources(user_choice, insufficient_resources)




