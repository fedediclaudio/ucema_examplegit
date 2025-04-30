# Este es el módulo numbers.py
def function1(first_number, second_number):
    return "UCEMA " + str(first_number) + " " + str(second_number)

# Esta es la función 2
def function2(first_number, second_number):
    return first_number + second_number

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
for i in range(10):
    print(fibonacci(i), end=" ")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
result1 = function1(first_number, second_number)
result2 = function2(first_number, second_number)
print(f"The result of function1 is: {result1}")
print(f"The result of function1 + 3 is: {result2+3}")
print(f"The result of function2 is: {result2}")