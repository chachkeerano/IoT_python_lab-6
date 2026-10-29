# Question 1: Count how many times each number occurs (without using count())

numbers = [2, 3, 2, 5, 3, 2, 5, 8]

# Empty dictionary to store the result
result = {}

# Go through every number in the list one by one
for num in numbers:
    # If we have already seen this number, add 1 to its count
    if num in result:
        result[num] += 1
    # Otherwise, this is the first time, so start its count at 1
    else:
        result[num] = 1

print(result)
