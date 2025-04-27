from py_compile import main

class Computer:
     # Constructor
     # Takes in a description, processor type, hard drive capacity, memory, operating system, year made and price
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
         # What methods will you need?
         # Display the computer's information
    def display_info(self):
        print(f"Description: {self.description}")
        print(f"Processor Type: {self.processor_type}")
        print(f"Hard Drive Capacity: {self.hard_drive_capacity} GB")
        print(f"Memory: {self.memory} GB")
        print(f"Operating System: {self.operating_system}")
        print(f"Year Made: {self.year_made}")
        print(f"Price: ${self.price}")

     # Update the price and operating system
    def update_price(self, new_price):
        self.price = new_price

     # Update the operating system
    def update_os(self, new_os):
        self.operating_system = new_os
     # Refurbish the computer
    def refurbish(self):
        self.description = "Refurbished " + self.description

