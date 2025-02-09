### NOTE: I rewrote the main.py file to test computer.py and oo_resale_shop.py based on the OOP approach ###

# Import the classes we wrote in Computer.py and oo_resale_shop.py
from computer import Computer
from oo_resale_shop import ResaleShop

# Test code taken and then modified from main.py 
def main():

    # First, let's make a computer (so that we can change the price and OS)
    computer = Computer("Mac Pro (Late 2013)",
                        "3.5 GHc 6-Core Intel Xeon E5",
                        1024, 64,
                        "macOS Big Sur", 2013, 1500
                        )
    
    # Create a shop
    shop = ResaleShop()

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    
    # Add it to the resale store's inventory
    print("Buying", computer.description)
    computer_id = shop.buy(computer)
    print("Adding to inventory...")
    print("Done.\n")

    # Update the price
    new_price = 1500
    print("Updating the price of", computer.description, "to", new_price)
    computer.update_price(new_price)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n") 

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(computer_id, new_OS)
    print("Done.\n") 

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")   

    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    shop.sell(computer_id)
    print("Done.\n")    

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Sell it again to see if an error message is printed
    print("Selling Item ID:", computer_id)
    shop.sell(computer_id) # Console: Item 0 not found. Please select another item to sell. 
    print("Done.\n")


    # Check inventory again (after selling) to see if an error message is printed
    print("Checking inventory...")
    shop.print_inventory() # Console: No inventory to display.
    print("Done.\n") 

    # Refurbish again to see if an error message is printed
    new_OS = "MacOS Sequoia"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(computer_id, new_OS) # Item 0 not found. Please select another item to refurbish.
    print("Done.\n")


    
# Calls the main() function when this file is run
if __name__ == "__main__": main()
