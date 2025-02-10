from py_compile import main


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
    def __init__(self, description,
    processor_type,
    hard_drive_capacity,
    memory,
    operating_system,
    year_made,
    price):
            self.description = str
            self.processor_type = processor_type
            self.hard_drive_capacity = hard_drive_capacity
            self.memory = memory
            self.operating_system = operating_system,
            self.year_made = year_made
            self.price = price
         # You'll remove this when you fill out your constructor

    # What methods will you need?
        
    def display_info(self):
         
         print("Description: self.description")
         print("Processor Type: Processor_type")
         print("Hard Drive Capacity: self.hard_drive_capcity")
         print("Memory: self.memory")
         print("Operating System: self.operating_system")
         print("Year Made: self.year_made")
         print("Price: self.price")
# create a varaible to update the price of the computer
    def update_price(self, new_price):
         
         self.price = new_price
# change/update the operating system
    def update_os(self, new_os):
         self.operating_system = new_os
# refurbishing 
    def refurbish(self):
         self.description = "refurbish" + self.description

if __name__ == "__main__": 
     main()
# computer instance 
     Comp = Computer(
        "Mac Pro (Late 2023)",
        "3.5 GHc 12-Core Intel W",
        1080, 64,
        "macOS M Series", 2023, 1700)
# show the final price/ OS
     Comp.update_price(1800)
     Comp.update_os("macOS Ventura")
     
     



    

