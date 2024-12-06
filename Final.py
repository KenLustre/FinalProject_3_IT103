def menu():
    print(f"\nWelcome to the Currency Converter!\n")
    print(f"1. Convert Currency \n2. Add Custom Exchange Rate \n3. Exit")

def custom_exchange_rate():
    print(f"\nAdd Custom Exchange Rate:\n")
    input_name = input(f"Enter the Name of the Currency (e.g., Korean Won, Japanese Yen): ")
    input_value = input(f"Enter the Value of your Currency in USD Dollars: ")

    if input_value.replace('.', '', 1).isdigit() and input_value.count('.') <= 1:
        value_in_usd = float(input_value)
        if value_in_usd > 0:  
            currency.append(input_name)
            value.append(value_in_usd)
            print(f"Successfully added: {input_name} with a value of {value_in_usd} USD.\n")
        else:
            print("Invalid value. The value must be greater than 0.\n")
    else:
        print("Invalid value. Please enter a valid number.\n")


def list_of_currencies():
    print("\nAvailable Currencies:")
    for i in range(len(currency)):
        print(f"{i + 1}. {currency[i]}")
    print("")

def conversion():
    from_currency = input("Enter the number corresponding to the currency you'd like to convert from: ")
    to_currency = input("Enter the number corresponding to the currency you'd like to convert to: ")

    if from_currency.isdigit() and to_currency.isdigit():
        from_index = int(from_currency) - 1
        to_index = int(to_currency) - 1
        if 0 <= from_index < len(currency) and 0 <= to_index < len(currency):
            amount = input(f"Enter the amount in {currency[from_index]} to convert: ")

            
            if amount.replace('.', '', 1).isdigit() and amount.count('.') <= 1:
                amount = float(amount)
                total = (amount / value[from_index]) * value[to_index]
                print(f"({currency[from_index]}) {amount} to {currency[to_index]} is {total:.2f}")
            else:
                print("Invalid amount. Please enter a valid number.")
        else:
            print("One or both of the numbers entered are out of range. Please try again.\n")
    else:
        print("Invalid input. Please enter numbers corresponding to the currencies.\n")


currency = ["United States Dollar", "Philippine Peso", "Japanese Yen", "Euro"]
value = [1, 57.8748, 150.184, 0.94801]

while True:
    menu()
    user_menu = input(f"\nChoose your option: ")

    if user_menu == "1":
        while True:
            print(f"\nPlease choose what currency you would like to convert")
            print(f"(Please note that our foreign exchange rates are based on OANDA Rates™.)")
            list_of_currencies()
            conversion()
            loop = input("Would you like to convert again? [Yes/No]: ")
            if loop.lower() == "no":
                break
            elif loop.lower() == "yes":
                continue
            else:
                print("Invalid input. Returning to the main menu.\n")
                break
        
    elif user_menu == "2":
        while True:
            custom_exchange_rate()
            loop = input("Would you like to add another Custom Exchange Rate? [Yes/No]: ")
            if loop.lower() == "no":
                break
            elif loop.lower() == "yes":
                continue
            else:
                print("Invalid input. Returning to the main menu.\n")
                break

    elif user_menu == "3":
        print(f"\nExiting the program. Thank you!\n")
        break

    else:
        print(f"\nInvalid option. Please type only between 1, 2, or 3.\n")
