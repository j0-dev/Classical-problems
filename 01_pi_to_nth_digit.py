
# Find Pi to the Nth Digit  - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

import math

def nth(n):
    pi = math.pi
    return(round(pi, n))

n = int(input("\nFINDING PI TO THE N DIGIT // Please enter how many decimal places you would like to round to: "))
print(nth(n))

    # Only gives floating point precision












