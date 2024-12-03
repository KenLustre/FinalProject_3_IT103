print(f"\nWelcome to the Currency Converter!\n")
print(f"1. Convert Currency \n2. Add Custom Exchange Rate \n3. Exit")
user_menu = int(input(f"\nChoose your option: "))

currency = []
value = []

def menu():
    print(f"\nWelcome to the Currency Converter!\n")
    print(f"1. Convert Currency \n2. Add Custom Exchange Rate \n3. Exit")

def custom_exchange_rate():
    print(f"Add Custom Exchange Rate:\n")
    input_name = input(f"Enter the Name of the Currency (e.g., Korean Won, Japanese Yen): ")
    input_value = input(f"Enter the Value of your Currency in USD Dollars: ")
    
    # Validate the value input
    if input_value.replace('.', '', 1).isdigit() and input_value.count('.') <= 1:
        value_in_usd = float(input_value)
        currency.append(input_name)
        value.append(value_in_usd)
        print(f"Successfully added: {input_name} with a value of {value_in_usd} USD.\n")
    else:
        print("Invalid value. Please enter a valid number.\n")

while user_menu != 3:
    if user_menu == 1:
        print(f"Please choose what currency you would like to convert (Please note that our foreign exchange rates are based on OANDA Rates™.)\n") 
        print("Available Currencies:")
        print(f"1. United States Dollar \n2. Philippine Peso \n3. Japanese Yen \n4. Euro")
        
        # Display custom currencies starting from index 5
        if currency:  
            for index in range(len(currency)):
                print(f"{index + 5}. {currency[index]}")  

        # Ask the user to choose an option again
        menu()  
        try:
            user_menu = int(input(f"\nChoose your option: "))
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")
            continue  # Skip the rest of the loop and prompt again

    elif user_menu == 2:
        custom_exchange_rate()
        
        loop = input("Would you like to add another Custom Exchange Rate? [Yes / No]: ")
        print("")
        if loop.lower() == "no":
            menu()  
            try:
                user_menu = int(input(f"\nChoose your option: "))
            except ValueError:
                print("Please enter a valid number (1, 2, or 3).")
                continue  # Skip the rest of the loop and prompt again
        elif loop.lower() == "yes":
            continue  # Go back to adding custom exchange rate

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
        break  # Exit the loop if the option is invalid

print(f"\nExiting the program. Thank you!\n")
