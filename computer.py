### NOTE: I rewrote the main.py file to test computer.py and oo_resale_shop.py based on a the OOP approach ###

class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    #1. Update the price of a computer
    def update_price(self, new_price: float): 
        self.price = new_price
        print("Price updated to:", new_price)
    
    #2. Update the OS of a computer
    def update_os(self, new_os:str):
        self.operating_system = new_os
        print("OS updated to:", new_os)
 