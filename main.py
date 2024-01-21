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

#TODO: 1. If user type "report" print amount of ingredients left
#TODO: 2.  Ask for coins if user choose one of the coffee menu
#TODO: 3.  Create Calculate function to check if coins and the price of coffee menu matches
#TODO: 4.  If money matches with the menu price,  print "Here is your {menu}" and give changes back.
#TODO: 5.  if money surplus, print "Here is {change} in change.
#TODO: 6.  If shortage, refund and print "Not enough money, refunded"
#TODO: 7.  After the coffee made, deduct the amount of resources from resources dictionary
#TODO: 8.  When user order a coffee, check if there are enough resources for the menu selected
#TODO: 9.  If resources are not enough, print the resource that is not enough.
#TODO: 10.  Loop through until user type "off"
