# Question 3: Swap keys and values of a dictionary

data = {'a': 1, 'b': 2, 'c': 3}

# New dictionary where old values become keys and old keys become values
swapped = {}

for key, value in data.items():
    swapped[value] = key

print(swapped)
