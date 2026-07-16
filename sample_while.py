condition = True 

while condition: 
    a = int(input("Emter a number:"))
    b = int(input("Enter another number:"))

    add = a + b
    print(f"{a} + {b} = {add}")

    print(" .................................")
    print("Do you still want to calculate?")
    response = input("Enter 'yes' to continue or 'no' to exit: ")
    if response == "yes":
        response = True
    else: 
        condition = False 