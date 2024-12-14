age = int(input("Insert your age: "))

if age < 5:
    print("You are too young for this.")
elif 5 <= age <= 18:
    print("You are a child or teenager.")
else:
    print("You are an adult.")
