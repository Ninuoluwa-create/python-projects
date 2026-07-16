def returnsomething():
    return 2 + 2
    


value = returnsomething()
print(value)


def add_three_numbers(a, b, c):
   return  a + b + c



def add_four_numbers(a, b, c, d):
    add = a + b + c + d
    return add

value = add_three_numbers (55, 66, 76)
print(f"Their sum is: {value}")



num1 = (input ("Enter a number"))
num2 = (input ("Enter a second number"))
num3 = (input ("Enter a third number"))

the_sum = add_three_numbers(num1, num2, num3)
print(f"The sum is: {add_three_numbers(num1, num2, num3)}")