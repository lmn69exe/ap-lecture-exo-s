letter1 = input("Insert the first letter: ")
letter2 = input("Insert the second letter: ")
letter3 = input("Insert the third letter: ")

letters = [letter1, letter2, letter3]
letters.sort()

print(f"The middle letter is {letters[1]}")
