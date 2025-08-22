# Restaurant Menu Project

menu = {
    'Pizza': 199,
    'Pasta': 170,
    'Burger': 99,
    'Noodles': 180,
    'Salad': 80,
    'Cold Coffee': 120,
    'Hot Coffee': 70,
    'Orange Juice': 50,
}

def show_menu():
    print("\nHere is our delicious menu:\n")
    for item, price in menu.items():
        print(f"{item}: Rs{price}")

def take_order():
    '"Take customer order and return the total'''
    total = 0
    item = input("\nEnter the name of item you want to order: ")
    if item in menu:
        total += menu[item]
        print(f" {item} has been added to your order.")
    else:
        print(f" Sorry, {item} is not available!")
    return total

# Main program
print(" Welcome to PYTHON Restaurant ")
show_menu()

order_total = take_order()

another_order = input("\nDo you want to add another item? (Yes/No): ")
if another_order.lower() == "yes":
    order_total += take_order()

print(f"\n The total amount of your order is Rs{order_total}.")
