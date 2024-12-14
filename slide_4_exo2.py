word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the third word: ")

if word1 <= word2 and word1 <= word3:
    first_word = word1
elif word2 <= word1 and word2 <= word3:
    first_word = word2
else:
    first_word = word3

print(f"The word that comes first alphabetically is: {first_word}")
