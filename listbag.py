"""
File: listbag.py

A list-based implementation of bags
"""

class ListBag(object):

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        pass

    # Accessor methods
    def isEmpty(self):
        """Returns True if the bag is empty, or False otherwise."""
        pass
    
    def __len__(self):
        """Returns the number of items in self."""
        pass

    def __str__(self):
        """Returns the string representation of self."""
        pass

    def __iter__(self):
        """Supports iteration over a view of self."""
        pass

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        pass

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        pass

    def count(self, item):
        """Returns the number of instances of item in self."""
        return self.items.count(item)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass

    def add(self, item):
        """Adds item to self."""
        pass

    def remove(self, item):
        """Remove item from self.
        Raises KeyError if item is not in self."""
        pass


def main():

    lyst = list(range(1, 11))
    print("The list of items added:", lyst)
    b = ListBag(lyst)
    print("The bag's size:", len(b))
    print("The bag's string:", b)
    print("The bag is empty:", b.isEmpty())
    print("4 is in the bag:", 4 in b)
    print("0 is in the bag:", 0 in b)
    b.add(7)
    print("Add 7 in bag")
    print("The bag's string:", b)
    b.remove(10)
    print("Remove 10 from bag")
    print("The bag's string:", b)
    print("How many instances of 7?", b.count(7))
    c = ListBag(b)
    print("c = ListBag(b)")
    print("b == c?", b == c)
    d = ListBag([22, 4])
    print("d = ListBag(22, 4)")
    print("b == d?", b == d)
    e = b + d
    print("e = b + d")
    print("bag e's string:", e)
    c.clear()
    print("c.clear()")
    print("bag c's string:", c)

if __name__ == "__main__":
    main()