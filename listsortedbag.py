"""
File: listsortedbag.py

A list-based implementation of sorted bag
"""

from listbag import ListBag

class ListSortedBag(ListBag):

    # Constructor
    def __init__(self, sourceCollection=None):
        """Create a list to store items in ascending order"""
        pass

    def __contains__(self, item):
        """Returns True if item is in self, or False
        otherwise. Use binary search"""
        pass

    def __add__(self, other):
        """Returns a new sorted bag containing the
        contents of self and other."""
        pass

    def add(self, item):
        """Adds item to self."""
        pass

def main():
    lyst = [8, 2, 4, 7, 6, 1]
    print("The list of items added is:", lyst)
    b = ListSortedBag(lyst)
    print("The bag's size:", len(b))
    print("The bag's string:", b)
    print()
    print("Searching for 6")
    print("6 is in the bag:", 6 in b)
    print()
    print("Searching for 3")
    print("3 is in the bag:", 3 in b)
    print()
    print("Add 5 in bag")
    b.add(5)
    print("The bag's string:", b)
    print()
    print("c = ListSortedBag(3, 4)")
    c = ListSortedBag([3, 4])
    print()
    print("d = b + c")
    d = b + c
    print("bag d's string:", d)

if __name__ == "__main__":
    main()