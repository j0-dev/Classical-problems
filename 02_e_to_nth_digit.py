
# Find e to the Nth Digit - Just like the previous problem, but with e instead of Pi. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

import decimal as d

def e(num, dp):
    rounded = round(num, dp)
    return rounded

x = d.Decimal(input("Number: "))
dp = int(input("How many DP: "))

print(f"Your number to {dp} decimal places = {e(x, dp)}")
