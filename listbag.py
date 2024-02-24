# Nicole Thomas
# Lab05
# February 23, 2024,


"""
File: listbag.py

A list-based implementation of bags
"""


class ListBag(object):

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = []
        if sourceCollection:
            self.items.extend(sourceCollection)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the bag is empty, or False otherwise."""
        return len(self.items) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ",".join(map(str, self.items)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        return iter(self.items)

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        new_bag = ListBag(self.items)
        new_bag.items.extend(other.items)
        return new_bag

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        return set(self.items) == set(other.items)

    def count(self, item):
        """Returns the number of instances of item in self."""
        return self.items.count(item)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = []

    def add(self, item):
        """Adds item to self."""
        self.items.append(item)

    def remove(self, item):
        """Remove item from self.
        Raises KeyError if item is not in self."""
        try:
            self.items.remove(item)
        except ValueError:
            raise KeyError(f"{item} not in the bag")


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
