#========Importing fuctions==========
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product 
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost


    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        return f"Shoe: country = {self.country}, code = {self.code}, product = {self.product}, cost = {self.cost}, quantity = {self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes
    '''
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                    country, code, product, cost, quantity = line.strip().split(',')
                    shoe = Shoe(country, code, product, float(cost), int(quantity))
                    shoe_list.append(shoe)
        return shoe_list
    except FileNotFoundError:
        print("Error: The file inventory.txt has not been found. ")
        return []

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    print("\n Enter shoe details: ")
    country = input("Country: ")
    code = input("Shoe Code: ")
    product = input("Shoe Name: ")
    cost = float(input("Cost of Shoe: "))
    quantity = int(input("Quantity of Shoe: "))

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

    with open("inventory.txt", "a") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")
        print("New shoe has been added successfully. ")

def view_all(shoes_list):
    '''
     This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''
    shoe_dictionary = [vars(shoe) for shoe in shoes_list]

    print("=====Current Stock======")
    print(tabulate(shoe_dictionary, headers="keys", tablefmt="grid"))

def re_stock(shoes_list):   
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    lowest_qty_shoe = min(shoes_list, key=lambda x: x.quantity)
    print(f"{lowest_qty_shoe.product} currently has the lowest stock with only {lowest_qty_shoe.quantity}left. ")

    re_stock_decision = input(f"Would you like to restock {lowest_qty_shoe.product}? Enter (yes/no): ").lower()
    if re_stock_decision == "yes":
        try:
            add_qty = int(input("How much stock would you like to order: "))
            lowest_qty_shoe.quantity += add_qty

            with open("inventory.txt", "w") as file:
                file.write("country,code,product,cost,quantity\n")
                for shoe in shoe_list:
                    file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
            print("Stock has been updated successfully. ")
        except ValueError:
            print("Invalid quantity. Please enter a whole number for shoe quantity. ")

def search_shoe(shoes_list, shoe_code):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    shoe_code = input("What is the product code of the shoe you are looking for: ")
    shoe_code = shoe_code.lower()
    for shoe in enumerate(shoes_list, start = 1):
        if shoe.shoe_code.lower() == shoe_code:
            print("====Shoe Details====")
            print(f"Country: {shoe.country}, Shoe code: {shoe.code}, Shoe Name: {shoe.product}, Shoe Cost: {shoe.cost}, Shoe Stock: {shoe.quantity}.")
            return shoe
    return None 

def value_per_item(shoe_lists):
    '''
    This function will calculate the total value for each item and print this information on the console for all the shoes.
    '''
    print("_"*25)
    for shoe in shoe_lists:
        total_value = shoe.cost * shoe.quantity
        print(f"Shoe {shoe.product} with code {shoe.code} has the total value of {total_value}")

def highest_qty(shoes_list):
    '''
    This function will find the shoe with the highest quantity and suggest it be put on sale
    '''
    highest_qty_shoe = max(shoes_list, key=lambda x: x.quantity)
    print(f"\n{highest_qty_shoe.product} with code {highest_qty_shoe.code}, currently has the highest stock and should be put on SALE! ")


#==========Main Menu=============
'''
Main menu that executes each function above.
'''
def main():

    shoes_list = read_shoes_data()
    while True:
        print("\n======== Nike Inventory Program ==========")
        print("1. View all shoes")
        print("2. Re-stock low inventory")
        print("3. Search shoe")
        print("4. Add a shoe")
        print("5. View stock value")
        print("6. View which stock to put on sale")
        print("7. Exit program")

        menu_choice = int(input("Please select on of the options above: "))
        if menu_choice == 1:
            view_all(shoes_list)
        elif menu_choice == 2:
            re_stock(shoes_list)
        elif menu_choice == 3:
            search_shoe(shoes_list)
        elif menu_choice == 4:
            capture_shoes(shoes_list)
        elif menu_choice == 5: 
            value_per_item(shoes_list)
        elif menu_choice == 6:
            highest_qty(shoes_list)
        elif menu_choice == 7:
            print("Exiting Program...")
            break
        else:
            print("Invalid menu option, pleae enter a valid option...")

main()

#=======References=========#
# I used datacamp.com for additional information on the tabulate function for this program