# MSIT 501 - Project 4
#
# Initial code developed by: Frank J. Mitropoulos
#
# Final code implemented by: Paisley Samuel


import pickle  # pickle makes it SO easy to load/save data from/to disk.


class Item:
    """
        This class models an Item in a a collection.
        An item has a category, description, value and quantity.
        For example: Antique, Desk, 250.00, 1
    """

    def __init__(self, category, desc, value, quant):
        """
           This is the constructor for the Item class. It creates an Item object
           from the parameters passed in by the user.
           Note that self must be used in order to refer to the object's properties

           This constructor should NOT need any modifications
        """
        self.category = category
        self.desc = desc
        self.value = value
        self.quant = quant

    def display(self):
        """
            This method simply displays the item properties in a nicely formatted manner.

            This method should NOT need any modifications.
        """
        print("{:<30}{:<18}{:8.2f}{:7d}".format(self.desc, self.category, self.value, self.quant))


class Collection:
    def __init__(self):
        self.items = []

    def addItem(self, category, desc, value, quant):
        new_item = Item(category, desc, value, quant)
        self.items.append(new_item)

    def __str__(self):
        s = ""
        for item in self.items:
            s = s + str(item) + "\n"
        return s

    def displayAllItems(self):
        print("{:<30}{:<20}{:9}{:10}".format("Description", "Category", " Value", " Amount"))
        print("-" * 70)
        for item in self.items:
            item.display()
        print()

    def displayAllCategories(self):
        print("Categories")
        print("-" * 12)
        categories = []
        for item in self.items:
            categories.append(item.category)
        unique_categories = []
        for category in categories:
            if category not in unique_categories:
                unique_categories.append(category)
        print(*unique_categories, sep="\n")
        print()

    def displayAllItemsForCategory(self, category):
        print(f"Displaying items in the category '{category}':")
        print("{:<30}{:<18}{:8}{:7}".format("Description", "Category", " Value", " Amount"))
        print("-" * 65)
        for item in self.items:
            if category in item.category:
                item.display()
        print()

    def displayItemsOverValue(self, value):
        print("Displaying items over $", '{:.2f}'.format(value))
        print("{:<30}{:<18}{:8}{:7}".format("Description", "Category", " Value", " Amount"))
        print("-" * 65)
        for item in self.items:
            if item.value > value:
                item.display()
        print()

    def displayItemFromDescription(self, desc):
        print("{:<30}{:<18}{:8}{:7}".format("Description", "Category", " Value", " Amount"))
        print("-" * 65)
        for item in self.items:
            if item.desc == desc:
                item.display()
        return

    def displayCollectionValue(self):
        total_value = 0
        for item in self.items:
            total_value = total_value + (item.quant * item.value)
        print("\nYour current collection value is $",'{:.2f}\n'.format(total_value))
        print()


def printMenu():
    print("")
    print("1. Display all items in my collection")
    print("2. Display the categories of my items")
    print("3. Display all items in a given category")
    print("4. Search for an item by description")
    print("5. Add a new item to my collection")
    print("6. Display all items above a given value")
    print("7. Calculate the total value of my collection")
    print("S. Save to disk")
    print("L. Load data from disk")
    print("Q. Quit")
    print()


# This is the main function that drives the program
# This function will be called when you run the program
# Modify this function as you see fit.
# Remember to do error checking.
#
# This function is already implemented to display the menu,
# get input from the user and call the appropriate Collection class methods

def main():
    stuff = Collection()
    print()
    print('{:^62s}'.format('Welcome to Collection Manager!'))
    print("_"*62)
    while True:
        printMenu()
        selection = input("Please enter a selection: ").strip().upper()
        if selection not in ['1', '2', '3', '4', '5', '6', '7', 'S', 'L', 'Q']:
            print("Invalid selection. Please enter a valid menu option.\n")
            continue
        if selection == '1':
            stuff.displayAllItems()
        elif selection == '2':
            stuff.displayAllCategories()
        elif selection == '3':
            category = input("Enter category: ").strip().title()
            stuff.displayAllItemsForCategory(category)
        elif selection == '4':
            itemToFind = input("Enter item's description: ").strip().title()
            stuff.displayItemFromDescription(itemToFind)
        elif selection == '5':
            try:
                cat = input("Enter the new item's category: ").strip().title()
                desc = input("Enter the new item's description: ").strip()
                value = eval(input("Enter the new item's value: "))
                quant = eval(input("Enter the new item's quantity: "))
                stuff.addItem(cat, desc, value, quant)
                print("Item added\n")
            except NameError:
                print("Invalid value. Please try again.")
        elif selection == '6':
            try:
                value = eval(input("Enter the value: "))
                stuff.displayItemsOverValue(value)
            except NameError:
                print("\nInvalid value. Please try again.\n")
        elif selection == '7':
            stuff.displayCollectionValue()
        elif selection == 'S':
            pickle.dump(stuff, open("stuff.pickle", "wb"))
            print("Data saved...\n")
        elif selection == 'L':
            stuff = pickle.load(open("stuff.pickle", "rb"))
            print("Data loaded...\n")
        else:
            print()
            print("_"*62)
            print()
            print('{:^62s}'.format("Thank you for using Collection Manager!\n\n"))
            break


# This line of code runs the main function above automatically when you run the program.

if __name__ == "__main__":
    main()
