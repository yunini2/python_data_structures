"""
File: timing1.py
Prints the running times for problem sizes that double, using a sigle loop
File:counting.py
Prints the number of iterations for problems sizes that double, using a nested loop
File: countfib.py
Prints the number of calls of a recursive Fibonacci function with problem sizes that double.

"""
# 度量算法的运行时间
import time

problemSize = 1000000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(5):
    start = time.time()
    # The start of the algorithm
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1
    # The end of the algorithm
    elapsed = time.time() - start
    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2

"""
Problem Size         Seconds
     1000000           0.309
     2000000           0.470
     4000000           0.969
     8000000           2.050
    16000000           4.254
"""


problemSize = 1000
print("%12s%15s" % ("Problem Size", "Iterations"))
for count2 in range(5):
    number = 0
    # The start of the algorithm
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            number += 1
            work += 1
            work -= 1
        # The end of the algorithm
        print("%12d%16.3f" % (problemSize, number))
        problemSize *= 2


from python_data_structures.ch1_python_base.numberguess import Counter
def fib(n, counter):
    """Count the number of calls of the Fibonacci"""
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n-1, counter) + fib(n-2, counter)
problemSize = 2
print("%12s%15s" % ("ProblemSize", "Calls"))
for count3 in range(5):
    counter = Counter()
    # The start of the algorithm
    fib(problemSize, counter)
    # The end of the algorithm
    print("%12d%15s" % (problemSize, counter))
    problemSize *= 2
"""
 ProblemSize          Calls
           2              1
           4              5
           8             41
          16           1973
          32        4356617
"""

# 复杂度分析

# 搜索算法--min
def indexOrderMin(lyst):
    """Returns the index of the minimum item."""
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex
al_min = indexOrderMin([5,2,9,10,5])    

# 顺序搜索一个列表
def sequentialSearch(target, lyst):
    """Returns the positon of the target item if found, or -1 otherwise."""
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1
al_order = sequentialSearch(5, [5,2,9,10,5])

# 二叉树搜索
def binarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1
al_binary_tree = binarySearch(1, [1, 5,2,9,10,5])

# 比较数据项
class SavingAccount(object):
    """This class represents a savings account with the owner's name, PIN, and balance."""
    def __init__(self, name, pin, balance = 0.0):
        self._name = name
        self._pin = pin
        self._balance = balance
    def __lt__(self, other):
        return self._name < other._name
    # Other methods,including __eq__
s1 = SavingAccount("Ken", "1000", 0)
s2 = SavingAccount("Bill", "1001", 30)
print(s1 < s2)

# 排序算法
def swap(lyst, i, j):
    """Exchanges the items at position i and j"""
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
    return lyst

# 选择排序
def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            lyst_sort =  swap(lyst, minIndex, i)
        i += 1
    return lyst_sort
a = selectionSort([5, 3, 1, 2, 4])

# 冒泡排序
def bubblesort(lyst):
    n = len(lyst)
    while n >1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                lyst_bubble = swap(lyst, i, i-1)
            i += 1
        n -= 1
    return lyst_bubble
a_bubble = bubblesort([5, 3, 1, 2, 4])
# 插入排序，没看懂。。。
