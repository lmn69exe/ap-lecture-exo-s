# First part
num = int(input("Insert a number: "))

if num%2 == 0:
    print(f"{num} is an even number!")
else:
    print(f"{num} is an odd number!")

# Second part
age = int(input("Insert your age: "))

if age > 18:
    print("You are ana adult!")
    print("Now go pay your taxes")
else:
    print("You are a minor!")