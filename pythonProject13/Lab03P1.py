# Nicole Thomas
# February 12, 2024,
# Finding second-largest item in a list

def main():
    list1 = [2, 8, 7, 5, 4, 1, 6]
    second_largest = find_second_largest(list1)
    print("list1", list1)
    print("Second largest item in list1:", second_largest)
    print()
    list2 = [2, 8, 8, 5, 4, 1, 6]
    second_largest = find_second_largest(list2)
    print("list1:", list2)
    print("Second largest item in list2:", second_largest)


def find_second_largest(my_list):
    if len("list1") < 2:
        return "List should have at least two elements."


largest = second_largest = float('-inf')

for num in list():
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("There is no second largest element in the list.")
else:
    print("second_largest item in list2:", second_largest)

# Example usage:
input_list = [2, 8, 7, 5, 4, 1, 6]
result = find_second_largest(input_list)
print(f"The second largest item is: {result}")
if __name__ == "__main__":
    main()
