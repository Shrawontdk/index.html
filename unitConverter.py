measurement = []
def meters_to_feet(meter):
    feet = meter*3.28084
    print(f"the feet is {feet}")
def feet_to_meters(feet):
    meter = feet / 3.028084
    print(f"the meter is {meter}")

def kilograms_to_pounds(kg):
    pound = kg * 2.2    
    print(f"the pound is {pound}")

def pounds_to_kilograms(pound):
    kg = pound / 2.2    
    print(f"the kg is {kg}")

def celsius_to_fahrenheit(celsius):
    fahrenheit= (celsius * (9/5) + 32)
    print(f"the fahrenheit is {fahrenheit}")

def fahrenheit_to_celsius(fahrenheit):
    celsius= (celsius * (9/5) + 32)
    print(f"the fahrenheit is {celsius}")

        
if __name__ == "__main__":
    print("Welcome to the unit converter\n")

    while True:
        print("Options:")
        print("1. Convert meters to feet")
        print("2. Convert feet to meters")
        print("3. Convert kilograms to pounds")
        print("4. Convert pounds to kilograms")
        print("5. Convert Celsius to Fahrenheit")
        print("6. Convert Fahrenheit to Celsius")
        print("7. Quit")




        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
           meter = float(input("Enter meter: "))
           meters_to_feet(meter)
        
        elif choice == "2":
            feet = float(input("Enter feet: "))
            feet_to_meters(feet)
        elif choice == "3":
            kg = float(input("Enter Kilogram: "))
            kilograms_to_pounds(kg)

            
        elif choice == "4":
            pound = float(input("Enter Pound: "))
            pounds_to_kilograms(pound)
        elif choice == "5":
            celsius = float(input("Enter Celsius: "))
            celsius_to_fahrenheit(celsius)
        elif choice == "6":
            fahrenheit = float(input("Enter Fahrenheit: "))
            fahrenheit_to_celsius(fahrenheit)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, 5, 6 or 7.\n")
