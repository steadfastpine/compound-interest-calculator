# This example demonstrates usage of the CompoundInterest class.


# Import the compoundinterest.py file

from compoundinterest import *


# Create an object from the class, input the 
# Format: CompundInterest(principle,rate,compounds_per_year,years)

test1 = CompoundInterest(5000,.03,12,6)


# Print the total calculated amount
print(test1.total)
