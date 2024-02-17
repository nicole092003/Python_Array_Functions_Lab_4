# Nicole Thomas
# LabCollectionsP2.py
# February 3, 2024

import random

# (a) Use a for loop and a random integer generator to generate 10 random integers in 1 through 15.
# Store the random integers in a list and then convert the list to a tuple. Display the tuple.
random_integers = [random.randint(1, 15) for _ in range(10)]
random_tuple = tuple(random_integers)
print("Random Tuple:", random_tuple)

# (b) Create a new tuple. Copy the first three elements of the tuple in part (a) to this tuple. Display this tuple.
tuple_part_b = random_tuple[:3]
print("Tuple Part B:", tuple_part_b)

# (c) Create a new tuple. Copy the last three elements of the tuple in part (a) to this tuple. Display this tuple.
tuple_part_c = random_tuple[-3:]
print("Tuple Part C:", tuple_part_c)

# (d) Concatenate the two tuples in part (b) and part (c). Display the concatenated tuple.
concatenated_tuple = tuple_part_b + tuple_part_c
print("Concatenated Tuple:", concatenated_tuple)

# (e) Sort the concatenated tuple. Display the sorted tuple.
sorted_tuple = tuple(sorted(concatenated_tuple))
print("Sorted Tuple:", sorted_tuple)
