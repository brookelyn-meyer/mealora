
from database import add_grocery_to_database, get_all_groceries

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
def show_groceries():
    groceries = get_all_groceries()

    print()
    print("===== Grocery List =====")

    for grocery in groceries:
        print(f"ID: {grocery[0]}")
        print(f"Name: {grocery[1]}")
        print(f"Quantity: {grocery[2]}")
        print(f"Location: {grocery[3]}")
        print(f"Expires: {grocery[4]}")
        print()

# calls the show_groceries function with the groceries parameter from the groceries dictionary
show_groceries()

# create a program that asks the user to
# 1. Enter grocery name:
# 2. Enter quantity:
# 3. Enter Location:
# 4. Enter expiration date:

# this function cleans up the code by putting all of the user input variables in one place, and creating a new dictionary for the grocery information, then returns it.
def get_grocery_information():
    grocery_name = input("Enter grocery name: ")
    quantity = input("Enter quantity: ")
    location = input("Enter location: ")
    expiration_date = input("Enter expiration date: ")

    grocery_information = {
        "name": grocery_name,
        "quantity": quantity,
        "location": location,
        "expiration_date": expiration_date
    }

    return grocery_information

# this function checks if the user inputs yes, then it calls the get grocery information function which helps keep it organized, and appends it to the end of the groceries
# dictionary. Then prints out the grocery added with the information, then it asks again if you want to add another grocery item and if you type anything other than yes that means no.
# empty print statement to make the code look nicer, then it prints updated grocery list and shows the groceries. loop ends and we print the grocery list and add the groceries so
# that they will be saved
def add_grocery(groceries):
    user_input = "yes"

    while user_input == "yes":
        grocery_information = get_grocery_information()
        add_grocery_to_database(
        grocery_information["name"],
        grocery_information["quantity"],
        grocery_information["location"],
        grocery_information["expiration_date"]
)

        print(f"Grocery Added: {grocery_information['name']}")

        user_input = input(
            "Do you want to add another grocery? yes/no: "
        ).lower()

    print()
    print("Updated Grocery List:")
    show_groceries()

    
    print(  )
    print(f"Updated Grocery List:")
    show_groceries()


add_grocery(groceries)



