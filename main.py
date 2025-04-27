# Import a few useful containers from the typing module
from computer import Computer
from oo_resale_shop import ResaleShop

def main():
    shop = ResaleShop()
    
    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer.description)
    print("Adding to inventory...")
    computer_id = shop.buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print(shop.get_inventory())
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print(f"Refurbishing Item ID: {computer_id}, updating OS to {new_OS}")
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
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()