from computer import Computer

class ResaleShop:

    inventory : list = []

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
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price, inventory):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        self.inventory = inventory
        
    # What methods will you need?

    def buy(self):
        self.inventory.append(self)
        return self.inventory.index(self)
         
    # computer_instance = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
    # self.inventory.append(self)
    #  print(f"New computer '{description}' added to inventory.")
    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
        # def sell(self, description, price):
        #  if Comp.description == description:

    def get_inventory(self):
        return self.inventory