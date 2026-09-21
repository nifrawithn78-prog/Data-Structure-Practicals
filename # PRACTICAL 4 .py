# PRACTICAL 4 - NUMPY

# 1. Create a NumPy Array
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])
print("Array:", numbers)

# 2. Basic Operations on Array
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])
print("Original array:", numbers)
print("Addition:", numbers + 5)
print("Subtraction:", numbers - 5)
print("Multiplication:", numbers * 2)

# 3. Find Maximum and Minimum
import numpy as np

numbers = np.array([25, 10, 45, 30, 15])
print("Array:", numbers)
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

# 4. Slice a NumPy Array
import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Original array:", numbers)
print("First five elements:", numbers[0:5])

# 5. Filter Array Values
import numpy as np

numbers = np.array([20, 45, 60, 75, 30, 90])
result = numbers[numbers > 50]
print("Values greater than 50:", result)