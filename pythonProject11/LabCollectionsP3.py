# Nicole Thomas
# LabCollectionsP3.py
# February 4, 2024

import random

# (a) Generate 5 random integers between 1 and 10, inclusive. Store in set1. Display the set.
set1 = set(random.sample(range(1, 11), 5))
print("Set1:", set1)

# (b) Generate 5 random integers between 1 and 10, inclusive. Store in set2. Display the set.
set2 = set(random.sample(range(1, 11), 5))
print("Set2:", set2)

# (c) Find and display the union of set1 and set2.
union_set = set1.union(set2)
print("Union of Set1 and Set2:", union_set)

# (d) Find and display the intersection of set1 and set2.
intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:", intersection_set)

# (e) Find and display the symmetric difference between set1 and set2.
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference between Set1 and Set2:", symmetric_difference_set)
