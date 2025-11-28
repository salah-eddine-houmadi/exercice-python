# #pr

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()
        print(f"Total lines: {len(lines)}")
except FileNotFoundError:
    print(f"Error: {filename} not found.")

# #pr

customer = input("Enter customer name: ")
item = input("Enter item: ")
price = input("Enter price: ")

record = f"Customer: {customer}, Item: {item}, Price: ${price}\n"

with open("sales.txt", "a") as file:
    file.write(record)

print("Record written to sales.txt")

#pr

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"Error: {filename} not found.")

#pr

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

try:
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#pr

while True:
    value = input("Enter a number: ")
    try:
        number = int(value)
        print("You entered:", number)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

#pr

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)
except Exception as e:
    with open("error_log.txt", "a") as file:
        file.write(str(e) + "\n")
    print("Error logged to file.")

#pr

print("File content from notes.txt:")

try:
    with open("notes.txt", "r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("notes.txt not found.")
