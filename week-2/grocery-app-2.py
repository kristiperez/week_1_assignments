
from shopping_list import ShoppingList
from grocery_item import GroceryItem

shopping_lists = []

user_input = ""

while user_input != "q":

    if user_input == "1":
        for index in range(0,len(shopping_lists)):
            shopping_list = shopping_lists[index]
            print(f"{index+1} - {shopping_list.title}")
            for index in range(0,len(shopping_list.items)):
                item_list = shopping_list.items[index]
                print(f"{item_list.title} - {item_list.quantity}")
            
    elif user_input == "2":

        title = input("Enter a title for your shopping list: ")
        address = input("Enter an address for shopping list: ")

        shopping_list = ShoppingList(title, address)

        shopping_lists.append(shopping_list)
        
        for index in range(0,len(shopping_lists)):
            shopping_list = shopping_lists[index]
            print(f"{index+1} - {shopping_list.title}")

    elif user_input == "3":

        shopping_list_number = int(input("Enter the shopping list number to add items to: "))
        title = input("Enter a grocery item: ")
        price = input("Enter a price for the grocery item: ")
        quantity = input("Enter a quantity for the grocery item: ")

        grocery_item = GroceryItem(title,price,quantity)

        shopping_list_to_add_number_to = shopping_lists[shopping_list_number -1]

        shopping_list_to_add_number_to.items.append(grocery_item)

        for index in range(0,len(shopping_lists)):
            shopping_list = shopping_lists[index]
            print(f"{shopping_list.title}")
            for index in range(0,len(shopping_list.items)):
                item_list = shopping_list.items[index]
                print(f"{item_list.title} - {item_list.quantity}")
                #print(shopping_list.items[index].title) ----> could do this instead of the 2 lines above

        
    user_input = input("Enter 2 to input a shopping list, and 3 to enter a grocery item. Otherwise press q to quit or 1 to display your shopping lists: ")
