import time

# Pizazo's Pizza: A Fictional Company
# Please do not tamper.
# THIS IS A COPYRIGHTED PROGRAM. ALL RIGHTS RESERVED. (JK)
# Format: PZ + [Size (1-3)] + [Type (1-4)] + [Dining (1-3)] + [Count (1-9)] -> e.g., PZ1121 (Length: 6)
# ON JIT HUB. I MEAN HIT. I MEAN KIT. I MEAN... FIT HUB. NO, JUST...GITHUB!

def app():
    """Text-based app to generate a Pizazo Code"""
    print("\n" + "=" * 40)
    print("       WELCOME TO THE PIZAZO APP")
    print("=" * 40)
    print("Let's build your custom Pizazo Code.")
    
    print("\n--- Step 1: Choose Size ---")
    print("1 - Small")
    print("2 - Medium")
    print("3 - Large")
    size_choice = input("Enter size number (1-3): ")
    
    print("\n--- Step 2: Choose Flavor ---")
    print("1 - Vegetable")
    print("2 - American Cheese")
    print("3 - Margherita")
    print("4 - Cheese 'n' corn")
    type_choice = input("Enter flavor number (1-4): ")
    
    print("\n--- Step 3: Dining Option ---")
    print("1 - Dine-In")
    print("2 - Takeaway")
    print("3 - Delivery")
    dining_choice = input("Enter dining option (1-3): ")
    
    print("\n--- Step 4: Quantity ---")
    count_choice = input("How many pizzas would you like? (Enter a number): ")
    
    generated_code = f"PZ{size_choice}{type_choice}{dining_choice}{count_choice}"
    
    print("\n[ SUCCESS ]")
    print("Your official Pizazo Code is:")
    print(f"CODE: {generated_code}")
    print("Write this down and use it in the main ordering system.")
    print("=" * 40 + "\n")


def pizza_order():
    """Main system to process a Pizazo Code and simulate preparation time"""
    print("\nWelcome! To Pizazo's Pizza! The best pizza in town, with a little pizaz!")
    print("Please enter your pizazo code below to queue your order.")
    pizazo_code = input("Pizazo Code: ").upper()
    
    def check_pizazo_code(code):
        validity = False
        
        if code.startswith("PZ") and len(code) >= 6:
            sizes = {"1": "Small", "2": "Medium", "3": "Large"}
            types = {"1": "Vegetable", "2": "American Cheese", "3": "Margherita", "4": "Cheese 'n' corn"}
            dining_options = {"1": "Dine-In", "2": "Takeaway", "3": "Delivery"}
            
            size_digit = code[2]
            type_digit = code[3]
            dining_digit = code[4]
            count_digit = code[5:] 
            
            if size_digit in sizes and type_digit in types and dining_digit in dining_options and count_digit.isdigit():
                size = sizes[size_digit]
                pizza_type = types[type_digit]
                dining_mode = dining_options[dining_digit]
                count = int(count_digit)
                pizza_word = "Pizza" if count == 1 else "Pizzas"
                
                print(f"\n[ORDER CONFIRMED] You have ordered {count} {size} {pizza_type} {pizza_word} for {dining_mode}.")
                
                if dining_digit == "3":
                    time_map = {"1": 25, "2": 30, "3": 35}
                else:
                    time_map = {"1": 5, "2": 10, "3": 15}
                
                seconds_per_pizza = time_map[size_digit]
                total_seconds = seconds_per_pizza * count
                
                print(f"[STATUS] Initializing {dining_mode.lower()} sequence. Total ETA: {total_seconds} seconds.")
                
                for remaining in range(total_seconds, 0, -1):
                    print(f"\r[PROCESSING] Time remaining: {remaining}s...", end="", flush=True)
                    time.sleep(1) 
                    
                print(f"\n[SUCCESS] Sequence complete! Your {dining_mode.lower()} order is ready. NOM NOM NOM\n")
                
                validity = True
            else:
                print("\n[ERROR] Sorry, but your pizazo code is invalid. Please check the menu digits and try again.\n")
        else:
            print("\n[ERROR] Sorry, but your pizazo code format is invalid. It should start with PZ followed by at least 4 digits.\n")
            
        return validity

    check_pizazo_code(pizazo_code)


def main():
    while True:
        print("--- PIZAZO'S PIZZA ---")
        print("1. Open Pizazo App (Create a Code)")
        print("2. Enter a Pizazo Code (Place an Order)")
        print("3. Exit System")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            app()
        elif choice == '2':
            pizza_order()
        elif choice == '3':
            print("\nPlease Come Again! Thank you for choosing Pizazo's Pizza!")
            break
        else:
            print("\n[ERROR] Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()