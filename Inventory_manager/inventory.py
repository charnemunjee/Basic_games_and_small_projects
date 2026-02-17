# The purpose of the code is to
# create an inventory manager
# for a Nike shoe store

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """
        This function will create a Nike shoe object with this data
        :param country: The country the show was made in
        :param code: The shoe code
        :param product: The type of shoe
        :param cost: The cost of the shoe
        :param quantity: The number of pairs of Nike shoes in stock
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
       """
       This function will return the cost of the shoe
       """
       return self.cost

    def get_quantity(self):
       """This function will return the
       number of pairs of Nike shoes in stock
       """
       return self.quantity

    def __str__(self):
        shoe_info = (f"\nShoe Country: {self.country}, Code: {self.code},"
                     f" Product: {self.product}, Cost: {self.cost}, "
                     f"Quantity: {self.quantity}\n")
        return shoe_info


# The shoe list will be used to store a list of objects of shoes.

shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    """
    This function will open the file inventory.txt
    and read the data from this file. The function creates shoe objects with this data
    and append these object into the shoes list. Each line in this file represents
    data to create one object of shoes.
    """ 

    try:
        shoe_list.clear()
        with open('inventory.txt', 'r') as inventory:
            inventory_list = inventory.readlines()
            inventory_list = inventory_list[1:]

            for item in inventory_list:
                item = item.split("\n")[0].split(",")
                item[3] = float(item[3])
                item[4] = int(item[4])
                shoe = Shoe(country=item[0], code=item[1],
                            product=item[2], cost=item[3],
                            quantity=item[4])
                shoe_list.append(shoe)
            return shoe_list

    except FileNotFoundError:
        print("Inventory file not found. Please check the path.")

def capture_shoes():
    """
    This function allows the user to input data
    about a shoe and use this data to create a shoe object,
    append this object inside the shoe list and add the
    information to the inventory.txt file.
    """

    while True:
        user_input = input("Would you like to capture data? (y/n): ").lower()
        if user_input == "y":
            shoe_code = input("Please enter the shoe code: ")
            shoe_country = input("Please enter the shoe country: ")
            shoe_product = input("Please enter the shoe product: ")
            shoe_cost = float(input("Please enter the shoe cost: "))
            shoe_quantity = int(input("Please enter the shoe quantity: "))
            new_shoe = Shoe(shoe_country, shoe_code, shoe_product,
                            shoe_cost, shoe_quantity)
            shoe_list.append(new_shoe)

            with open('inventory.txt', 'a') as inventory:
                inventory.write(f"\n{new_shoe.country},{new_shoe.code},"
                                f"{new_shoe.product},"
                                f"{new_shoe.cost},{new_shoe.quantity}")
        else:
            break

def view_all():
    """
    This function iterates over the shoes list and
    prints the details of the shoes returned from the __str__
    function.
    """
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    """
    This function will finda the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. It asks the user if they
    want to add to this quantity of shoes and then update it.
    This quantity is then updated in the inventory.txt file.
    """

    shoe_min_index = 0
    shoe_min = int(shoe_list[0].quantity)
    for i in range(len(shoe_list)):
        if int(shoe_list[i].quantity) < shoe_min:
            shoe_min_index = i
            shoe_min = int(shoe_list[i].quantity)

    print(f"The shoe with the lowest stock levels is "
          f"{shoe_list[shoe_min_index].product} "
          f"at minimum stock level: "
          f"{shoe_list[shoe_min_index].quantity}")

    update_quantity = input("Would you like to "
                            "update the quantity of "
                            "shoes? (y/n): ").lower()
    if update_quantity == "y":
        shoe_update = int(input("How many pairs "
                                "of shoes do you want to add?: "))
        shoe_list[shoe_min_index].quantity = (
                shoe_list[shoe_min_index].quantity + shoe_update)
        print(f"The number of shoes in stock is now "
              f"{shoe_list[shoe_min_index].quantity}")
    with open('inventory.txt', 'r') as file:
        header = file.readlines()[0]

    with open('inventory.txt', "w+") as inventory:
        inventory.write(str(header))
        for shoe in shoe_list:
            inventory.write(f"{shoe.country},{shoe.code},"
                            f"{shoe.product},"
                            f"{shoe.cost},{shoe.quantity}\n")

def search_shoe():
    """
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    """

    shoe_exists = False
    shoe_search = input("Please enter the shoe code: ")
    i=0
    while not shoe_exists and i < len(shoe_list):
        if shoe_list[i].code == shoe_search:
            shoe_exists = True
            break
        else:
            i += 1

    if not shoe_exists:
        print("This shoe doesn't exist.")
    else:
        print(shoe_list[i])


def value_per_item():
    """
    This function will calculate the total value for each item.
    The formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    """
    
    stock_value_list = []
    total_stock_value = 0

    # use for loop to loop though the shoe list and
    # calculate total stock value for the shoe
    # and append to stock_value_list
    for shoe in shoe_list:
        shoe_value = shoe.quantity * shoe.cost
        total_stock_value += shoe_value
        stock_value_list.append({"Shoe product": shoe.product,
                                 "Stock Value": shoe_value})

    # print shoe and stock value
    print("")
    for  item in stock_value_list:
        print(item["Shoe product"],":", item["Stock Value"])
    print("")


def highest_qty():
    """
    This code determines the product with the highest quantity and
    prints this shoe as being for sale.
    """

    max_quantity = 0
    shoe_name = ""

    # loop through shoe list to find
    # the shoe with highest the quantity
    for i in range(len(shoe_list)):
        if int(shoe_list[i].quantity) > max_quantity:
            max_quantity = int(shoe_list[i].quantity)
            shoe_name = shoe_list[i].product


    string_shoe = (f"\nThe product with the highest "
                   f"quantity is: {shoe_name} with "
                   f"{max_quantity} shoes in stock. "
                   f"This shoe is for sale\n")
    print(string_shoe)


#==========Main Menu=============

# This while loop creates a menu that executes the functions above
read_shoes_data() # read in shoe data from inventory file
while True:
    print("Welcome to the inventory menu.")
    user_instruction = input("What would you like to do?\n"
          "1 - search for products by code\n"
          "2 - find the product with the lowest quantity\n"
          "3 - find the product with the highest quantity\n"
          "4 - calculate total value of each stock item\n"
          "5 - view all shoes\n"
          "6 - add new shoes to the inventory\n"
          "7 - exit the menu\n")

    if user_instruction == "1":
        search_shoe()
    elif user_instruction == "2":
        re_stock()
    elif user_instruction == "3":
        highest_qty()
    elif user_instruction == "4":
        value_per_item()
    elif user_instruction == "5":
        view_all()
    elif user_instruction == "6":
        capture_shoes()
    elif user_instruction == "7":
        exit()