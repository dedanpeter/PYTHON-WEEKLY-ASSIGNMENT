# electricity_bill.py
# Task 1: Electricity Bill Function

# A function that calculates the bill
def calculate_bill(units, cost):
    bill = units * cost
    return bill

# Ask the user for the numbers
units = float(input("Enter units consumed: "))
cost = float(input("Enter cost per unit: "))

# Call the function
result = calculate_bill(units, cost)

# Show the answer
print("Electricity bill:", result)
