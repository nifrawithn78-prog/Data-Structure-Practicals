# Programs 1-8 from the document
# Organized here as the first section of the 23-page material.

# 1. Create a 2D NumPy Array
import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr)

# 2. Find Shape of an Array
import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("Shape:", arr.shape)

# 3. Reshape an Array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = arr.reshape(2, 3)
print(new_arr)

# 4. Generate Random Numbers
import numpy as np
numbers = np.random.randint(1, 100, 10)
print(numbers)

# 5. Calculate Mean, Median and Standard Deviation
import numpy as np
marks = np.array([60, 70, 80, 90, 75])
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))

# 6. Group Students According to Course
import pandas as pd
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Course": ["BSc", "BCA", "BSc", "BCA"],
    "Marks": [80, 90, 70, 85]
}
df = pd.DataFrame(data)
result = df.groupby("Course")["Marks"].mean()
print(result)

# 7. Count Students in Each Course
import pandas as pd
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Course": ["BSc", "BCA", "BSc", "BCA"]
}
df = pd.DataFrame(data)
print(df["Course"].value_counts())

# 8. Find Top 3 Students
import pandas as pd
data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],
    "Marks": [75, 95, 65, 90, 85]
}
df = pd.DataFrame(data)
result = df.sort_values("Marks", ascending=False)
print(result.head(3))
