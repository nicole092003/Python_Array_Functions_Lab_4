# Nicole Thomas
# February 12, 2024,
# Counting Sort

def main():
    list1 = [8, 2, 4, 5, 4, 7, 2, 6, 8, 6, 2, 5, 6]
    list1_sorted = counting_sort(list1)
    print("list1 before sorting:", list1)
    print("list1 after sorting:", list1_sorted)


def counting_sort(my_list):
    if not my_list:
        return "List is empty."

    # Step 1: Find the smallest and largest items in the list
    smallest = min(my_list)
    largest = max(my_list)

    # Step 2: Create an empty list for the sorted version
    sorted_list = []

    # Step 3-4: Count the frequency and generate the sorted list
    for value in range(smallest, largest + 1):
        frequency = my_list.count(value)
        sorted_list.extend([value] * frequency)

    return sorted_list


if __name__ == "__main__":
    main()
