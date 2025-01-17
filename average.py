a = [10, 20, 30, 40, 50]

# Finding sum using built-in sum() function
totalSum = sum(a)

# Finding average using built-in sum() and len() functions
average = totalSum / len(a) if a else 0  # Avoid division by zero

print("Sum of the list:", totalSum)
print("Average of the list:", average)