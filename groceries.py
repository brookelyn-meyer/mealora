# list of groceries that are in stock

groceries = [
    {
        "name": "Ground Beef",
        "quantity": 1,
        "location": "Fridge",
        "expiration_date": "2026-07-27"
    },
    {
        "name": "Taco Seasoning",
        "quantity": 1,
        "location": "Pantry",
        "expiration_date": "2027-03-15"
    },
    {
        "name": "Tortillas",
        "quantity": 8,
        "location": "Pantry",
        "expiration_date": "2026-08-02"
    },
    {
        "name": "Shredded Cheese",
        "quantity": 1,
        "location": "Fridge",
        "expiration_date": "2026-07-29"
    },
    {
        "name": "Lettuce",
        "quantity": 1,
        "location": "Fridge",
        "expiration_date": "2026-07-25"
    },
    {
        "name": "Tomato",
        "quantity": 2,
        "location": "Counter",
        "expiration_date": "2026-07-26"
    },
    {
        "name": "Sour Cream",
        "quantity": 1,
        "location": "Fridge",
        "expiration_date": "2026-08-01"
    }
]



# prints a list of the groceries name, quantity, location, and when it expires
def show_groceries(groceries):
    print(  )
    print("===== My Groceries =====")
    print(  )
    for grocery in groceries:
        print(f"Name:", grocery["name"])
        print(f"Quantity:", grocery["quantity"])
        print(f"Location:", grocery["location"])
        print(f"Expires:", grocery["expiration_date"])
        print(  )


# calls the show_groceries function with the groceries parameter from the groceries dictionary
show_groceries(groceries)

# create a program that asks the user to
# 1. Enter grocery name:
# 2. Enter quantity:
# 3. Enter Location:
# 4. Enter expiration date:

def add_grocery(groceries):
    # asks the user to input the grocery name
    print(f"Enter grocery name:")
    grocery_name = input()
    print(f"Grocery Added: {grocery_name}")
    # asks the user to enter the quantity
    print(f"Enter quantity:")
    quantity = input()
    print(f"Updated Quantity: {quantity}")
    # asks the user to enter the location of the groceries
    print(f"Enter Location:")
    location = input()
    print(f"Location: {location}")
    #asks the user to enter the expiration date
    print(f"Enter expiration date:")
    expiration_date = input()
    print(f"Expiration date: {expiration_date}")

    print(f"Do you want to add more groceries?:")
    user_input = input().lower()
    while user_input == "yes":
            print(f"Enter another grocery:")
            new_grocery = input().lower()
            print(f"Grocery Added: {new_grocery}")
            # asks the user to enter the quantity
            print(f"Enter quantity:")
            quantity = input()
            print(f"Updated Quantity: {quantity}")
            # asks the user to enter the location of the groceries
            print(f"Enter Location:")
            location = input()
            print(f"Location: {location}")
            #asks the user to enter the expiration date
            print(f"Enter expiration date:")
            expiration_date = input()
            print(f"Expiration date: {expiration_date}")
            print("Do you want to add another grocery?")
            user_input = input().lower()
            # adds the new groceries to our groceries list!
            groceries.append({
            "name": new_grocery,
            "quantity": quantity,
            "location": location,
            "expiration_date": expiration_date
            })

    
    print(  )
    print(f"Updated Grocery List:")
    show_groceries(groceries)


add_grocery(groceries)



