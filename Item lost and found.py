#FINDIT - SMART LOST AND FOUND SYSTEM

items = []

def report_item():
    print("\n--- REPORT ITEM ---")

    item_type = input("Enter Lost or Found: ").lower()

    if item_type != "lost" and item_type != "found":
        print("Invalid item type!")
        return

    name = input("Enter Item Name: ")
    category = input("Enter Category: ")
    location = input("Enter Location: ")
    date = input("Enter Date: ")
    contact = input("Enter Contact: ")

    item = [item_type, name, category,
            location, date, contact, "Active"]

    items.append(item)

    print("\nItem reported successfully!")


def view_items():
    print("\n--- ALL REPORTED ITEMS ---")

    if len(items) == 0:
        print("No items reported yet.")
        return

    for i in range(len(items)):
        print("\nReport Number:", i + 1)
        print("Type:", items[i][0])
        print("Name:", items[i][1])
        print("Category:", items[i][2])
        print("Location:", items[i][3])
        print("Date:", items[i][4])
        print("Contact:", items[i][5])
        print("Status:", items[i][6])


def search_item():
    print("\n--- SEARCH ITEM ---")

    keyword = input("Enter Item Name: ").lower()
    found = False

    for item in items:
        if keyword in item[1].lower():
            print("\nMatching Item Found!")
            print("Type:", item[0])
            print("Name:", item[1])
            print("Location:", item[3])
            print("Contact:", item[5])
            print("Status:", item[6])
            found = True

    if found == False:
        print("Item not found!")


def return_item():
    view_items()

    if len(items) == 0:
        return

    number = int(input("\nEnter Report Number: "))

    if number >= 1 and number <= len(items):
        items[number - 1][6] = "Returned"
        print("Item marked as returned!")
    else:
        print("Invalid report number!")


def main():
    while True:
        print("\n==============================")
        print("     FINDIT LOST & FOUND")
        print("==============================")
        print("1. Report Lost or Found Item")
        print("2. View All Items")
        print("3. Search Item")
        print("4. Mark Item as Returned")
        print("5. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            report_item()

        elif choice == "2":
            view_items()

        elif choice == "3":
            search_item()

        elif choice == "4":
            return_item()

        elif choice == "5":
            print("Thank you for using FindIt!")
            break

        else:
            print("Invalid Choice! Try Again.")


main()
