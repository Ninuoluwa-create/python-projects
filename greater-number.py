num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}.")
elif num_1 < num_2:
    print(f"{num_2} is greater than {num_1}.")
else:
    print("Both numbers are equal.")