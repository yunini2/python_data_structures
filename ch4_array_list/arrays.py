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

a = Array(5)
len(a)
print(a)
for i in range(len(a)):
    a[i] = i + 1
for item in a: print(item)

# 二维数组
# 处理网格
# 定义Grid类
class Grid(object):
    """Represents a two-dimensional array"""
    def __init__(self, rows, columns, fillValue = None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fillValue)
    def getHeight(self):
        """Returns the number of rows"""
        return len(self._data)
    def getWidth(self):
        """Returns the number of columns"""
        return len(self._data[0])
    def __getitem__(self, index):
        """Supports two-dimensional indexing with [row][column]"""
        return self._data[index]
    def __str__(self):
        """Return a string representation of the grid"""
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self._data[row][col]) + " "
            result += "\n"
        return result
table = Grid(4, 5, 0)
print(table)
# 创建并初始化网络
sum = 0
for row in range(table.getHeight()):
    for column in range(table.getWidth()):
        sum += table[row][column]
print(sum)

# Go through rows
for row in range(table.getWidth()):
    # Go through columns
    for column in range(table.getWidth()):
        table[row][column] = int(str(row) + str(table))

# 定义一个单链表节点类
class Node(object):
    """Represents a singly linked node."""
    def __init__(self, data, next = None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next
# 使用单链表节点类
node1 = None
node2 = Node("A", None)
node3 = Node("B", None)

node1.next = node3 # AttributeError: 'NoneType' object has no attribute 'next'
node1 = Node("C", node3)
