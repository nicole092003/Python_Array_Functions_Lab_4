# Nicole Thomas
# Lab01BP3.py
# January 22, 2024


def calculate_total_pay(hourly_rate, hours_worked):
    # Calculate total pay based on hourly rate and hours worked
    total_pay = hourly_rate * hours_worked
    return total_pay


def main():
    # Open the payroll_data.txt file for reading
    with open("payroll_data.txt", "r") as file:
        # Read lines from the file
        lines = file.readlines()

        # Display header
        print("{:<10} {:<12} {:<12} {:<10}".format("Name", "Hourly Rate", "Hours Worked", "Total Pay"))
        print("=" * 44)

        # Process each line in the file
        for line in lines:
            # Split the line into three fields: last name, hourly rate, and hours worked
            fields = line.split()

            # Extract values from fields
            name = fields[0]
            hourly_rate = float(fields[1])
            hours_worked = float(fields[2])

            # Calculate total pay using the function
            total_pay = calculate_total_pay(hourly_rate, hours_worked)

            # Display employee information
            print("{:<10} ${:<11} {:<12} ${:<10.2f}".format(name, hourly_rate, hours_worked, total_pay))


# Call the main function to start the program
main()
