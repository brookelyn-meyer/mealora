from database import (
    add_grocery_to_database,
    get_all_groceries,
    delete_grocery_from_database
)



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
def add_grocery():
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





def delete_grocery():
    show_groceries()

    grocery_id = input("Enter the ID of the grocery you want to delete: ")

    deleted_rows = delete_grocery_from_database(grocery_id)

    if deleted_rows == 1:
        print("Grocery deleted successfully!")
    else:
        print("No grocery was found with that ID.")


def show_menu():
    print()
    print("===== MealOra =====")
    print("1. View groceries")
    print("2. Add grocery")
    print("3. Delete grocery")
    print("4. Exit")

    
def main():
    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            show_groceries()

        elif choice == "2":
            add_grocery()

        elif choice == "3":
            delete_grocery()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1 through 4.")

            

if __name__ == "__main__":
    main()