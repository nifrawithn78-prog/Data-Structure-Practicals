# Programs 9-16 from the document
# Organized here as the second section of the 23-page material.

# 9. Add a Result Column
import pandas as pd
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Marks": [75, 35, 65, 90]
}
df = pd.DataFrame(data)
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)
print(df)

# 10. Simple Bar Chart
import matplotlib.pyplot as plt
names = ["Rahul", "Priya", "Amit", "Sneha"]
marks = [75, 90, 65, 85]
plt.bar(names, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

# 11. Simple Line Graph
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 130, 180]
plt.plot(months, sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()

# 12. Simple Histogram
import matplotlib.pyplot as plt
marks = [50, 60, 65, 70, 70, 75, 80, 85, 90, 95]
plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")
plt.show()

# 13. Create a Linked List and Display Its Elements
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

current = n1
while current:
    print(current.data)
    current = current.next

# 14. Insert Node at the Beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(20)
head.next = Node(30)

new_node = Node(10)
new_node.next = head
head = new_node

current = head
while current:
    print(current.data)
    current = current.next

# 15. Insert Node at the End
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)

new_node = Node(30)
current = head
while current.next:
    current = current.next
current.next = new_node

current = head
while current:
    print(current.data)
    current = current.next

# 16. Delete Node from Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head.next = head.next.next

current = head
while current:
    print(current.data)
    current = current.next
