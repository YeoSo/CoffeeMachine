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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
"""
user = input(" What would you like? (espresso/latte/cappuccino): ")

money = 0
# If user type 'report', shows the status
if user == 'report':
    for ingredient, remain in resources.items():
        if 'coffee' in ingredient:
            print(f"{ingredient}: {remain}g")
        else:
            print(f"{ingredient}: {remain}ml")
    print(f"Money: ${money}")
"""

money = 0

while True:
    user = input(" What would you like? (espresso/latte/cappuccino): ")

    if user == 'off':
        print("Shutting off. Thank you for using the coffee machine.")
        break

    elif user == 'report':
        for ingredient, remain in resources.items():
            if 'coffee' in ingredient:
                print(f"{ingredient}: {remain}g")
            else:
                print(f"{ingredient}: {remain}ml")
        print(f"Money: ${money}")

    elif user in MENU:
        # Check if there are enough resources for the selected drink
        ingredients_needed = MENU[user]["ingredients"]
        insufficient_resources = False
        insufficient_ingredient = ""

        for ingredient, amount in ingredients_needed.items():
            if resources[ingredient] < amount:
                insufficient_resources = True
                insufficient_ingredient = ingredient
                break

        if not insufficient_resources:
            # Subtract resources and update money
            for ingredient, amount in ingredients_needed.items():
                resources[ingredient] -= amount
            money += MENU[user]["cost"]
            print(f"Here is your {user}. Enjoy!")

        if insufficient_ingredient:
            print(f"Apologies, we ran out of {insufficient_ingredient}.")

    else:
        print("Invalid choice. Please choose a valid option.")





# TODO: 1. If user type "report" print amount of ingredients left
# TODO: 2.  Ask for coins if user choose one of the coffee menu
# TODO: 3.  Create Calculate function to check if coins and the price of coffee menu matches
# TODO: 4.  If money matches with the menu price,  print "Here is your {menu}" and give changes back.
# TODO: 5.  if money surplus, print "Here is {change} in change.
# TODO: 6.  If shortage, refund and print "Not enough money, refunded"
# TODO: 7.  After the coffee made, deduct the amount of resources from resources dictionary
# TODO: 8.  When user order a coffee, check if there are enough resources for the menu selected
# TODO: 9.  If resources are not enough, print the resource that is not enough.
# TODO: 10.  Loop through until user type "off"