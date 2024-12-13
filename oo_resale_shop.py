from computer import Computer
from typing import Dict, Optional

class ResaleShop:

    # inventory and computer ID attributes
    inventory: list
    itemID: int

    # initializes the inventory
    def __init__(self, inventory, itemID):
        self.inventory = inventory
        self.itemID = itemID

    # buys a computer
    def buy(self, computer):
        self.inventory.append(computer)
        self.itemID += 1
        print(computer.description + "bought.")

    # sells a computer
    def sell(self, computer):
        if len(self.inventory) > 0:
            self.inventory.remove(computer)
            self.itemID -= 1
            print(computer.description + "sold.")
        else:
            print("There are no computers currently in inventory.")
    
    # prints the current inventory
    def print_inventory(self):
        if len(self.inventory) > 0:
            for computer in self.inventory:
                print(computer.description, 
                      computer.processor_type, 
                      computer.hard_drive_capacity, 
                      computer.memory, 
                      computer.operating_system, 
                      computer.year_made, 
                      computer.price)
        else:
            print("There are no computers currently in inventory.")

    # updates a computer's operating system
    def updateOS(self, computer, new_OS):
        if computer in self.inventory:
            computer.operating_system = new_OS
        else:
            print("Computer not in inventory.")

    # updates a computer's price
    def updatePrice(self, computer, new_price):
        if computer in self.inventory:
            computer.price = new_price
        else:
            print("Computer not in inventory.")
    
    # refurbishes a computer
    def refurbish(self, computer, new_OS):
        if computer in self.inventory:
            if computer.year_made < 2000:
                computer.price = 0
            elif computer.year_made < 2012:
                computer.price = 250
            elif computer.year_made < 2018:
                computer.price = 550
            else:
                computer.price = 1000

            if new_OS is not None:
                computer.operating_system = new_OS
    
        else:
            print("Computer not in inventory.")

def main():

    # makes first example computer
    my_computer = Computer(
        "2023 MacBook Pro",
        "Apple M3 Pro",
        994.66,
        36,
        "Sonoma",
        2023,
        1500)
    
    # makes second example computer
    your_computer = Computer(
        "2019 MacBook Pro",
        "Intel",
        256,
        16,
        "High Sierra",
        2019,
        1000)
    
    # creates the inventory and Resale Shop
    inventory = []
    my_ResaleShop = ResaleShop(inventory, itemID = 0)

    # buys both computers, returns inventory
    my_ResaleShop.buy(my_computer)
    my_ResaleShop.buy(your_computer)
    print("Your inventory currently consists of", 
          my_ResaleShop.inventory)

    # sells first computer, returns inventory
    my_ResaleShop.sell(my_computer)
    print("Computer sold!", 
          "Your inventory currently consists of", 
          my_ResaleShop.inventory)
    
    # updates OS of second computer
    my_ResaleShop.updateOS(your_computer, "Sonoma")

    # updates price of second computer
    my_ResaleShop.updatePrice(your_computer, 1000)

    # refurbishes second computer
    my_ResaleShop.refurbish(your_computer, "Sonoma")

if __name__ == "__main__":
    main()