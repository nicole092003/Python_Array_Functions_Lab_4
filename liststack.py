"""
File: liststack.py
A list-based implementation of stacks.
"""


class ListStack(object):
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        pass

    # Accessor methods
    def isEmpty(self):
        """Returns True if the stack is empty, or False otherwise."""
        pass
    
    def __len__(self):
        """Returns the number of items in the stack."""
        pass

    def __str__(self):
        """Returns the string representation of the stack."""
        pass

    def __iter__(self):
        """Supports iteration over a view of the stack."""
        pass


    def __add__(self, other):
        """Returns a new stack containing the contents
        of self and other."""
        pass


    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        pass

    def peek(self):
        """Returns the item at top of the stack.
        Raises IndexError if stack is empty."""
        pass

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass

    def push(self, item):
        """Inserts item at the top of the stack."""
        pass

    def pop(self):
        """Removes and returns the item at top of the stack.
        Raises IndexError if stack is empty."""
        pass

def main():
    lyst = [8, 2, 4, 7, 6, 1]
    print("The list of items added is:", lyst)
    b = ListStack(lyst)
    print("The stack's size:", len(b))
    print("The stack's string:", b)
    print()

    print("Pop")
    print("Item popped:", b.pop())
    print("The stack's string:", b)
    print()
    print("c = ListStack(b)")

    print("Push 5")
    b.push(5)
    print("The stack's string:", b)
    print()
    print("Item at top:", b.peek())
    print("The stack's string:", b)
    print()

    print("Push 3")
    b.push(3)
    print("The stack's string:", b)
    print()
    print("Item at top:", b.peek())
    print("The stack's string:", b)
    print()

    print("Pop")
    print("Item popped:", b.pop())
    print("The stack's string:", b)
    print()
    print("c = ListStack(b)")

    c = ListStack(b)
    print("b == c?", b == c)
    print()

    print("d = ListStack([1, 2, 3, 4, 5, 6])")
    d = ListStack([1, 2, 3, 4, 5, 6])
    print("b == d?", b == d)
    print()

    print("e = b + d")
    e = b + d
    print("Stack e's string:", e)
    print("Is e empty?", e.isEmpty())
    print()

    e.clear()
    print("Clear e")
    print("Is e empty?", e.isEmpty())
    print("Stack e's string:", e)

if __name__ == "__main__":
    main()