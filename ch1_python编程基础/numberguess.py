"""
Author: Lily
Plays game of guess the number with the user.
"""
import random

def main():
    """
    Input the bounds of the range of numbers and lets the user guess the computer's number
     until the guess is correct.
    """
    samller = int(input("Enter the smaller number:"))
    larger = int(input("Enter the larger number:"))
    myNumber = random.randint(samller, larger)

    count = 0
    while True:
        count += 1
        userNumber = int(input("Enter your guess:"))
        if userNumber < myNumber:
            print("too smaller")
        elif userNumber > myNumber:
            print("too large")
        else:
            print("You've got it in", count, 'tries!')
            break
if __name__ == "__main__":
    main()

# 循环语句
product = 1
for value in range(1, 11):
    product *= value
print(product)
# 字符串及其运算
"greater"[0]
# 遍历序列
testList = [67, 100, 22]
for item in testList:
    print(item)
for index in range(len(testList)):
    print(testList[index])
# 编写新函数
def first():
    second()
    print("Calling first")
def second():
    print("Calling second")
first()
# 递归函数
def displayRange(lower, upper):
    """Outputs the numbers from lower to upper"""
    while lower <= upper:
        print(lower)
        lower += 1
displayRange(1,5)
def displayRange(lower, upper):
    """Outputs the numbers from lower to upper"""
    if lower <= upper:
        print(lower)
        displayRange(lower + 1, upper)
def ourSum(lower, upper):
    """Returns the sum of the numbers from lower to upper"""
    if lower > upper:
        return 0
    else:
        return lower + ourSum(lower + 1, upper)
ourSum(1, 4)

def ourSum(lower, upper, margin = 0):
    """Returns the sum of the numbers from lower to upper,
    and oupute s trace or the arguments and return values
    on each call"""
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + ourSum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result
# 嵌套函数，第一个定义使用了一个嵌套的辅助函数
def factorial(n):
    """Returns the factorial of n."""
    def recurse(n, product):
        if n == 1: return product
        else: return recurse(n - 1, n * product)
    return recurse(n, 1)
factorial(5)
# 定义给定了第二个参数一个默认值
def factorial(n, product = 1):
    """Returns the factorial of n."""
    if n == 1: return product
    else: return factorial(n - 1, n * product)

import functools
product = functools.reduce(lambda x, y: x * y, range(1, 11))
# 捕获异常
"""
Author: Lily
Demonstrates a funciton that traps number format errors during input.
"""
def safeIntergerInput(prompt):
    """Prompts the user for an interger and returns the interger if it is well-formed.
    Otherwise, prints an error message and repeats this process."""
    inputString = input(prompt)
    try:
        number = int(inputString)
        return number
    except:
        print("Error in number format:", inputString)
        return safeIntergerInput(prompt)
if __name__ == "__main__":
    age = safeIntergerInput("Enter your age:")
    print("Your age is", age)

# 定义类
class Counter(object):
    """Models a counter."""
    # Class variable
    instances = 0 # 记录了所创建的Counter对象的数目

    # Constructor
    def __init__(self): # self是一个额外的参数，出现在参数列表的开始处
        """Sets up the counter."""
        Counter.instances += 1
        self.reset()
    # Mutator methods，修改器，通过修改对象的实例变量，来修改或改变对象的内部状态
    def reset(self): # 初始化单个变量
        """Sets the counter to 0."""
        self._value = 0
    def increment(self, amount = 1):
        """Adds amount to the counter."""
        self._value += amount
    def decrement(self, amount = 1):
        """Subtracts amount from the counter."""
        self._value -= amount
    # Accessor methods，访问器，直接查看或使用对象的实例变量的值，不修改值
    def getValue(self):
        """Returns the counter'values"""
        return self._value

    def __str__(self): # 把变量作为参数传递给str函数
        """Returns the string representation of the counter."""
        return str(self._value)
    def __eq__(self, other): # 比较两个运算符的对象相等性
        """Returns True if self equals other or False otherwise."""
        if self is other:return True
        if type(self) != type(object):return False
        return self._value == other._value



c1 = Counter()
print(c1)
c1.getValue()
str(c1)
c1.increment()
print(c1)
c1.increment(5)
print(c1)
c1.reset()
print(c1)
c2 = Counter()
print(c2.instances)
print(c1 == c1)
print(c1 == 0)
print(c1 == c2)
c2.increment()
print(c1 == c2)


