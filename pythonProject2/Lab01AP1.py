# Nicole Thomas
# Lab01AP1.py
# January 9,2024


# Ask user for inputs
hourly_wage = float(input("Please enter hourly wage: "))
regular_hours = int(input("Please enter hours worked: "))
overtime_hours = int(input("Please enter overtime hours worked: "))


# Calculate regular pay
def main():
    regular_pay = hourly_wage * regular_hours


# Calculate overtime pay
overtime_pay = overtime_hours * regular_hours * hourly_wage * 1.5

# Calculate total pay
total_pay = regular_hours + overtime_pay

print("Total weekly pay: ${:.1f}".format(total_pay))

main()
