# Write a Python script using map, filter, and reduce with lambda functions:
# Convert words to uppercase.
# Select words containing 'a'.
# Concatenate selected words.
# Example word list: ["python", "programming", "is", "fun", "lambda", "filter", "reduce", "map", "example", "practice"]

from functools import reduce

word_list = ["python", "programming", "is", "fun", "lambda", "filter", "reduce", "map", "example", "practice"]

# Convert words to uppercase

uppercase = list(map(lambda word: word.upper(), word_list))
print("Uppercase words: ", uppercase)

# Select words containing 'a'

words_with_a = list(filter(lambda word: 'A' in word, uppercase))
print("Words with A: ", words_with_a)

# Concatenate selected words

concatenated_words = reduce(lambda x, y: x + y, words_with_a)
print("Concatenated selected words: ", concatenated_words)