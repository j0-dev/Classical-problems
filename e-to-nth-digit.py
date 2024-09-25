
    # Find e to the Nth Digit - Just like the previous problem, but with e instead of Pi. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

# My solution:
import decimal as d

def e(num, dp):
    rounded = round(num, dp)
    return rounded

x = d.Decimal(input("Number: "))
dp = int(input("How many DP: "))

print(f"Your number to {dp} decimal places = {e(x, dp)}")



# Internet solution:
# The round() function doesn't work directly with the decimal.Decimal type for controlling decimal places the way you intend. Also, since you want to display e (Euler's number) to n decimal places, you need to generate e using decimal.Decimal

    # d.getcontext().prec = 102  # For example, limit to 100 decimal places

    # def calculate_e(dp):
    #     e_value = d.Decimal(1).exp()  # Calculate e
    #     return round(e_value, dp)

    # dp = int(input("How many decimal places: "))

    # # Ensure the limit on decimal places
    # if dp > 100:
    #     print("Limit exceeded! Maximum is 100 decimal places.")
    # else:
    #     print(f"e to {dp} decimal places = {calculate_e(dp)}")