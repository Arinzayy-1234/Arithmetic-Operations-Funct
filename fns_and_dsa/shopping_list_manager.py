
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice not in ['1', '2', '3', '4']:
            print  ("Please enter a valid choice (1-4).")
            continue

        if choice == '1':
            # Prompt for and add an item
            add_item = input(" Enter the item to add:").strip()
            shopping_list.append(add_item)
            print(f"The item {add_item} has been added")
            
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Enter the item you want to remove: ")
            counter = 0
            for item in shopping_list:
                if remove_item == item:
                    del shopping_list[counter]
                    print(f"The iten {remove_item} has been removed")
                    break
                else:
                    print("Item not found !!")
                counter += 1
            
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


