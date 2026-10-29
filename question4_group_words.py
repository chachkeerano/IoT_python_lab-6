# Question 4: Group words by their first letter

words = ['apple', 'ant', 'banana', 'ball', 'cat']

grouped = {}

for word in words:
    # Take the first letter of the word
    first_letter = word[0]

    # If this letter is not in the dictionary yet, create an empty list for it
    if first_letter not in grouped:
        grouped[first_letter] = []

    # Add the word to the list of its first letter
    grouped[first_letter].append(word)

print(grouped)
