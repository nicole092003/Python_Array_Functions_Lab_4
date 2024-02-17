# Nicole Thomas
# Lab01AP2.py
# January 9, 2024

# Ask user for number of copies

num_copies = int(input("Please enter number of copies purchased: "))
unit_price = int(input("What is the unit price of the product: "))


def main():
    # Number of copies purchased and unit price

    def calculate_total_price(unit_price):

        if num_copies <= 1 and num_copies <= 10:
            unit_price = 99
        elif 11 <= num_copies <= 50:
            unit_price = 89
        elif 51 <= num_copies <= 100:
            unit_price = 79
        else:
            unit_price = 69


total_price = unit_price * num_copies

print("Unit price: ${:.0f}".format(unit_price))
print("Total price: ${:.0f}".format(total_price))

main()
