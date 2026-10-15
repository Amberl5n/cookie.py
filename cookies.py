# cookies.py
# Author: Amberlyn
# Homework #2 - Cookie Recipe Calculator
# This program calculates ingredient amounts for a custom number of cookies

# Original recipe makes 48 cookies
ORIGINAL_COOKIES = 48
SUGAR_ORIGINAL = 1.5    # cups
BUTTER_ORIGINAL = 1.0   # cups
FLOUR_ORIGINAL = 2.75   # cups

# Ask user how many cookies they want
cookies_wanted = float(input("How many cookies do you want to make? "))

# Calculate the ratio
ratio = cookies_wanted / ORIGINAL_COOKIES

# Calculate needed ingredients
sugar_needed = SUGAR_ORIGINAL * ratio
butter_needed = BUTTER_ORIGINAL * ratio
flour_needed = FLOUR_ORIGINAL * ratio

# Display results
print(f"For {cookies_wanted} cookies, you need:")
print(f"Sugar: {sugar_needed:.2f} cups")
print(f"Butter: {butter_needed:.2f} cups")
print(f"Flour: {flour_needed:.2f} cups")