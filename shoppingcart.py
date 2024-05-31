print("Welcome to the Shopping Cart Program!")

item_list = []

menu_options = [
    "1. Add item",
    "2. View cart",
    "3. Remove item",
    "4. Compute total",
    "5. Quit"
]

new_Client = ""
total_price = 0

while new_Client != "Quit":
    menu = "\n".join(menu_options)

    cart = input(f"Please select one of the following:\n{menu}\n")
    if cart == "1":
        item = input("What item would you like to add? ")
        item_price = input(f"What is the price of '{item}'? $")
        item_list.append({"name": item, "price": float(item_price)})
        print(f"'{item}' has been added to the cart.\n")

    elif cart == "2":
        print("The contents of the shopping cart are:")
        for i, item in enumerate(item_list, start=1):
            print(f"{i}. {item['name']} - ${item['price']}")
        print()

    elif cart == "3":
        remove = input("What item would you like to remove? ")
        removed = False
        for i in range(len(item_list)):
            if item_list[i]['name'] == remove:
                removed_item = item_list.pop(i)
                print(f"'{removed_item['name']}' has been removed from the cart.")
                removed = True
                break

        if not removed:
            print(f"'{remove}' is not in the cart.")    
       
    elif cart == "4":
        total_price = 0  # Reset total price before computing
        for item in item_list:
            total_price += item['price']
        print("\nTotal price of all items:", total_price, "\n")


    elif cart == "Quit":
        new_Client = "Quit"

    else:
        print("Invalid option. Please select again.\n")


print("Thank you. Goodbye.")





