#pr
 
def greet():
    print("Hello, Lkhibra Academy!")

greet()

#pr

def welcome(name):
    print(f"Hello, {name}! welcome to lkhibra Academy")

welcome("sara")
welcome("Youssef")

#pr

def square(num):
    return num * num

result = square(5)

print(f"the square of 5 is {result}")

#pr

def greet(name="Student"):
    print(f"Hello, {name}!")

greet()

greet("Amnie")

#pr

academy = "LKhibra"

def show_academy():
    print(f"The best academy is {academy}!")

show_academy()

#pr

def show_message():
    message = "Lkibra Rocks!"
    print("Inside function", message)

show_message()

try:
    print("Outside function:", message)
except NameError as e:
    print("Error:", e)

#pr

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(f"Factorial of 5 is {result}")

#pr

def calculate(x,y):
    sum = x + y
    product = x * y
    return sum, product

sum_result, product_result = calculate(3,5)

print(f"Sum: {sum_result}, Product: {product_result}")
