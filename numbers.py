# Este es el módulo numbers.py
def function1(first_number, second_number):
    return "UCEMA " + str(first_number) + " " + str(second_number)

# Esta es la función 2
def function2(first_number, second_number):
    first_number = first_number * 2
    return first_number + second_number

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
result1 = function1(first_number, second_number)
result2 = function2(first_number, second_number)
print(f"The result of function1 is: {result1}")
print(f"The result of function2 is: {result2}")