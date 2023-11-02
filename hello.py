def is_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


user_input = int(input("Enter a number: "))
is_even_or_odd(user_input)

# next


def find_maximum(a, b, c):
    if a > b and a > c:
        print(f"{a} is maximim number")

    elif b > c > a and b > a > c:
        print(f"{b}" is maximum)

    else:
        print(f"{c} is maximum")


num1 = float(input("Enter a First Number:"))
num2 = float(input("Enter a Sec Number:"))
num3 = float(input("Enter a Third Number:"))
find_maximum(num1, num2, num3)

# next


def is_vowel(char):
    if char.lower() in 'aeiou':
        return True
    else:
        return False


user_input = input("Enter a character: ")
result = is_vowel(user_input)

if result:
    print(f"{user_input} is a vowel.")
else:
    print(f"{user_input} is a consonant.")

    # next


def is_leap_year(year):
    if (((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0)):
        return True
    else:
        return False


leapYear = int(input("Enter a year: "))
result = is_leap_year(leapYear)

if result:
    print(f"{leapYear} is a a leap year.")
else:
    print(f"{leapYear} is a not a leap year.")

# next


def calculate_discount():
    try:
        original_price = float(input("Enter the original price: "))
        discount_percentage = float(input("Enter the discount percentage: "))

        if discount_percentage > 50:
            discount_percentage = 50

        discounted_price = original_price - \
            (original_price * (discount_percentage / 100))

        return discounted_price
    except ValueError:
        return "Invalid input. Please enter valid numbers."
discounted_price = calculate_discount()
print(f"Discounted Price: {discounted_price}")


