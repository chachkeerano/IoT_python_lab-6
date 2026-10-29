# Question 2: Print every student who got the highest marks

marks = {
    'Ali': 85,
    'Sara': 95,
    'Ahmed': 95,
    'Noor': 78
}

# Step 1: Find the highest marks among all students
highest = max(marks.values())

# Step 2: Check each student and print only those with the highest marks
print("Toppers:")
for name, score in marks.items():
    if score == highest:
        print(name, "-", score)
