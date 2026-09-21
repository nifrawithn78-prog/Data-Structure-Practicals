# Programs 17-25 from the document
# Organized here as the third section of the 23-page material.

# 17. Search an Element in Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

search = int(input("Enter value to search: "))
current = head
found = False

while current:
    if current.data == search:
        found = True
        break
    current = current.next

if found:
    print("Element found")
else:
    print("Element not found")

# 18. Stack Using List
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)
print("Deleted:", stack.pop())
print("Stack after deletion:", stack)

# 19. Stack Using Menu
stack = []
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        stack.append(value)
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Deleted:", stack.pop())
    elif choice == 3:
        print("Stack:", stack)
    elif choice == 4:
        break
    else:
        print("Invalid choice")

# 20. Queue Using List
queue = []
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", queue)
print("Deleted:", queue.pop(0))
print("Queue after deletion:", queue)

# 21. Queue Using Menu
queue = []
while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        queue.append(value)
    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Deleted:", queue.pop(0))
    elif choice == 3:
        print("Queue:", queue)
    elif choice == 4:
        break
    else:
        print("Invalid choice")

# 22. Circular Queue
from collections import deque
queue = deque(maxlen=3)
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
queue.append(40)
print(queue)

# 23. Linear Search
numbers = [10, 20, 30, 40, 50]
search = int(input("Enter number: "))
found = False

for i in range(len(numbers)):
    if numbers[i] == search:
        print("Element found at position", i)
        found = True
        break

if not found:
    print("Element not found")

# 24. Binary Search
numbers = [10, 20, 30, 40, 50, 60]
search = int(input("Enter number: "))
low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == search:
        print("Element found")
        break
    elif search > numbers[mid]:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")

# 25. Bubble Sort
numbers = [50, 20, 40, 10, 30]
for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Sorted list:", numbers)

# 26. Selection Sort
numbers = [50, 20, 40, 10, 30]
for i in range(len(numbers)):
    minimum = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[minimum]:
            minimum = j
    numbers[i], numbers[minimum] = numbers[minimum], numbers[i]
print(numbers)

# 27. Insertion Sort
numbers = [50, 20, 40, 10, 30]
for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j = j - 1
    numbers[j + 1] = key
print("Sorted list:", numbers)

# 28. Recursion - Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter number: "))
print("Factorial:", factorial(num))

# 29. Recursion - Fibonacci Series
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter number of terms: "))
for i in range(n):
    print(fibonacci(i), end=" ")

# 30. Create a Simple Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(20)
root.right = Node(30)

print("Root:", root.data)
print("Left:", root.left.data)
print("Right:", root.right.data)

# 31. Tree Traversal - Inorder
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
inorder(root)

# 32. Dictionary as Key-Value Data Structure
student = {
    "RollNo": 101,
    "Name": "Rahul",
    "Marks": 85
}
print("Roll No:", student["RollNo"])
print("Name:", student["Name"])
print("Marks:", student["Marks"])

# 33. Count Frequency of Elements
numbers = [10, 20, 10, 30, 20, 10]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)

# 34. Word Frequency
text = "python data science python data"
words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

# 35. Set Operations
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)

# 36. Stack Using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

stack = None

new_node = Node(10)
new_node.next = stack
stack = new_node

new_node = Node(20)
new_node.next = stack
stack = new_node

current = stack
while current:
    print(current.data)
    current = current.next

# 37. Queue Using Linked List
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", queue)
queue.popleft()
print("After deletion:", queue)
