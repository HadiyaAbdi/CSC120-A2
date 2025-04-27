
from computer import Computer

class ResaleShop:

    inventory : list = []
    # How will you set up your constructor?
    # Constructor method initializes the inventory list
    # Takes in a list of computers
    def __init__(self):
        self.inventory = []
        
    # What methods will you need?

    # Takes in a Computer object, adds it to the inventory, returns the assigned item_id
    def buy(self, computer:Computer):
        self.inventory.append(computer)
        return self.inventory.index(computer)
    
    # Method to sell a computer by item_id
    def sell(self, item_id: int):
        if 0 <= item_id < len(self.inventory):
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    # method to refurbish a computer by its iteam_id
    def refurbish(self, item_id: int, new_os: str):
        if 0 <= item_id < len(self.inventory):
            computer = self.inventory[item_id]
            computer.refurbish()
            computer.update_os(new_os)
            if int(computer.year_made) < 2000:
                computer.update_price(0) # old to be sold, so donation only
            elif int(computer.year_made) < 2012:
                computer.update_price(250) # discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.update_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_price(1000) # recent stuff
        else:
            print(f"Item {item_id}", item_id, "not found. Cannot refurbish.")

    # method to get the current inventory
    def get_inventory(self):
        return [comp.display_info() for comp in self.inventory]
    
    # method to print the inventory
    def print_inventory(self):
        if self.inventory:
            for i, item in enumerate(self.inventory):
                print(f'Item ID: {i} : {item.description}')
        else:
            print("No inventory to display.")