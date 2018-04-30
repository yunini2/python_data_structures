class Array(object):
    """Represents an array."""
    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.fillValue is placed at each position."""
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)
    def __str__(self):
        """-> The string representation of the array"""
        return str(self._items)
    def __iter__(self):
        """Supports traversal with a for loop"""
        return iter(self._items)
    def __getitem__(self, index):
        """Subscript operator for access at index"""
        return self._items[index]
    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index"""
        self._items[index] = newItem

class Node(object):
    """Represents a singly linked node."""
    def __init__(self, data, next = None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next

class ArrayBag(object):
    """An array-based bag implementation."""
    # Class variable
    DEFAULT_CAPACITY = 10
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the contents of sourceCollection, if it's present."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self)==0, or False otherwise."""
        return len(self) == 0
    def __len__(self):
        """Returns the number of items in self."""
        return self._size
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        self._items[len(self)] = item
        self._size += 1
    # 完成迭代器
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1
    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"
    def __add__(self, other):
        """Returns a new bag containing the contents of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result
    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True
    # 完成remove方法
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        postcondition:item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + "not in bag")
        # Search for index of target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # Decrement logical size
        self._size -= 1
        # Check array memory here and decrease it if necessary




# 开发一个基于链表的实现
# 初始化结构数据
class LinkedBag(object):
    """A link-based bag implementation."""
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the contents of sourceCollection, if it's present."""
        self._items = None
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
    # 完成迭代器
    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self)==0, or False otherwise."""
        return len(self) == 0
    def __len__(self):
        """Returns the number of items in self."""
        return self._size
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next
    # 完成clear和add方法
    def add(self, item):
        """Adds item to self."""
        self._items = Node(item, self._items)
        self._size += 1
    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"
    def __add__(self, other):
        """Returns a new bag containing the contents of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result
    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        postcondition:item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + "not in bag")
        # Search for the node containing the target item
        # probe wil point to the target node, and trailer will point to the one before it,if it exists
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        # Unhook the node to be deleted, either the first one or the one thereafter
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        # Decrement logical size
        self._size -= 1

# 测试包的实现
def test(bagType):
    """Expects a bag type as an argument and runs som tests on objects of that type"""
    lyst = [2018, 61, 1739]
    print("The list of items added is:", lyst)
    b1 = bagType(lyst)
    print("Expect 3:", len(b1))
    print("Expect the bag's string:", b1)
    print("Expect True:", 2018 in b1)
    print("Expect False:", 2019 in b1)
    print("Expect the items on separate lines:")
    for item in b1:
        print(item)
    b1.clear()
    print("Expect {}:", b1)
    b1.add(289)
    b1.remove(289)
    print("Expect {}:", b1)
    b1 = bagType(lyst)
    b2 = bagType(b1)
    print("Expect True:", b1 == b2)
    print("Expect False:", b1 is b2)
    print("Expect two of each item:", b1 + b2)
    for item in lyst:
        b1.remove(item)
    print("Expect {}:", b1)
    print("Expect crash with KeyError:")
    b2.remove(99)

test(ArrayBag)
"""
test(ArrayBag)
The list of items added is: [2018, 61, 1739]
Expect 3: 3
Expect the bag's string: {2018, 61, 1739}
Expect True: True
Expect False: False
Expect the items on separate lines:
2018
61
1739
Expect {}: {}
Expect {}: {}
Expect True: True
Expect False: False
Expect two of each item: {2018, 61, 1739, 2018, 61, 1739}
Expect {}: {}
Expect crash with KeyError:
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 27, in test
  File "<input>", line 62, in remove
KeyError: '99not in bag'

"""

test(LinkedBag)
"""
The list of items added is: [2018, 61, 1739]
Expect 3: 3
Expect the bag's string: {1739, 61, 2018}
Expect True: True
Expect False: False
Expect the items on separate lines:
1739
61
2018
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 93, in test
  File "<input>", line 39, in __str__
  File "<input>", line 30, in __iter__
AttributeError: 'Array' object has no attribute 'data'

"""