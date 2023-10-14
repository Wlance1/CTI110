# This program calculates and displays travel expenses.
# Date10/14/2023
# CTI-110 P1HW2 - Travel Expense
# William Lance Whitley


budget = float(input("Enter budget: $"))


destination = input("Enter your travel destination: ")


gas_expense = float(input("How much do you think you will spend on gas? $"))


accommodation_expense = float(input("Approximately, how much will you need for accommodation: $"))


food_expense = float(input("Last, how much do you need for food $"))


total_expenses = gas_expense + accommodation_expense + food_expense


remaining_budget = budget - total_expenses


print("\nTravel Expense Summary")
print("Destination:", destination)
print("Budget: $", budget)
print("Gas Expense: $", gas_expense)
print("Accommodation Expense: $", accommodation_expense)
print("Food Expense: $", food_expense)
print("Total Expenses: $", total_expenses)
print("Remaining Budget: $", remaining_budget)
