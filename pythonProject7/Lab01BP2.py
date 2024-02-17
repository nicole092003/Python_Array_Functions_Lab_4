# Nicole Thomas
# Lab01B2.py
# January 22, 2024


def main():
    # Call get_user_input to get kWh used and customer type
    kWh_used, customer_type = get_user_input()

    # Call bill_calculator with the obtained values and display the result
    energy_charge = bill_calculator(kWh_used, customer_type)
    print("Energy Charge: ${:.2f}".format(energy_charge))


def get_user_input():
    while True:
        try:
            # Ask the user to enter number of kWh used
            kWh_used = float(input("Enter the number of kWh used: "))
            if kWh_used < 0:
                raise ValueError("Please enter a non-negative value for kWh used.")

            # Ask the user to enter customer type (R for residential, B for business)
            customer_type = input("Enter customer type (R for residential, B for business): ").upper()
            if customer_type not in ['R', 'B']:
                raise ValueError("Please enter either 'R' for residential or 'B' for business.")

            # Return kWh used and customer type
            return kWh_used, customer_type

        except ValueError as e:
            print("Invalid input. {}".format(e))


def bill_calculator(kWh_used, customer_type):
    # Define the energy charge rates
    residential_rate = 0.12
    business_rate = 0.16

    # Calculate energy charge based on customer type
    if customer_type == 'R':
        energy_charge = kWh_used * residential_rate
    else:
        energy_charge = kWh_used * business_rate

    return energy_charge


# Call the main function to start the program
main()
