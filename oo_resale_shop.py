class ResaleShop:
    
    # What attributes will it need?
    inventory: list # A list of all the computers our store has to offer

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    #1. Buy a new computer
    def buy(self, new_computer: dict):
        self.inventory.append(new_computer)
        return self.inventory.index(new_computer) #Return the index (item id) of the new computer
    
    #2. Sell a computer
    def sell(self, item_id: int):
        if 0 <= item_id < len(self.inventory): #Note: Changed from "is not None" to prevent issues of negative numbers or indexes that don't exist within the inventory.
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    #3. Print the inventory
    def print_inventory(self):
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")

    #4. Refurbish a computer
    def refurbish(self,item_id: int, new_os: str = None ):
        self.item_id = item_id
        self.new_os = new_os
        if 0 <= item_id < len(self.inventory): #Note: Changed from "is not None" to prevent issues of negative numbers or indexes that don't exist within the inventory.
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

