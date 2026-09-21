# PRACTICAL 1

# 1. Insert an Element in an Array
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
print("Original Array:", arr)
position = int(input("Enter position to insert (1 to {}): ".format(n + 1)))
element = int(input("Enter element to insert: "))
arr.insert(position - 1, element)
print("Array after insertion:")
print(arr)

# 2. Access a Matrix Using Recursive Call
def display(matrix, rows, cols, i, j):
    if i == rows:
        return
    print(matrix[i][j], end=" ")
    if j == cols - 1:
        print()
        display(matrix, rows, cols, i + 1, 0)
    else:
        display(matrix, rows, cols, i, j + 1)

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)
print("\nMatrix:")
display(matrix, rows, cols, 0, 0)

# 3. Addition and Multiplication of Two 2D Arrays
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
A = []
B = []
print("Enter elements of Matrix A")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)
print("Enter elements of Matrix B")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    B.append(row)
print("\nAddition of Matrices")
for i in range(rows):
    for j in range(cols):
        print(A[i][j] + B[i][j], end=" ")
    print()
print("\nMultiplication of Matrices")
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        total = 0
        for k in range(cols):
            total = total + A[i][k] * B[k][j]
        row.append(total)
    result.append(row)
for i in range(rows):
    for j in range(cols):
        print(result[i][j], end=" ")
    print()

# 4. Transpose of a 2D Array
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix elements")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)
print("\nOriginal Matrix")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()
print("\nTranspose Matrix")
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()