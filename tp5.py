# Exercise 1 — Representing an Object
car = {
    "brand": "Honda",
    "model": "Civic",
    "year": 2018
}

print(car["model"])


#Exercise 2 — Update a Product
product = {
    "name": "Latte",
    "price": 3.5,
    "available": True
}

product["price"] += 1.0  
print(product)

#Exercise 3 — Safe Access with .get()
student = {
    "name": "Youssef",
    "grade": "A"
}

age = student.get("age")

if age is None:
    print("Age is missing from the data")
else:
    print(age)

#Exercise 4 — Course Structure
course = {
    "title": "Web Development",
    "chapters": ["HTML Basics", "CSS Styling", "JavaScript Intro", "React Fundamentals"]
}

print(course["chapters"][3])  

#Exercise 5 — Employee Summary
employee = {
    "name": "Nada",
    "role": "Designer",
    "salary": 9000
}

for key, value in employee.items():
    print(f"{key}: {value}")

# Exercise 6 — Simple Login System
users = {
    "salah": "pass123",
    "nada": "design99"
}

username = input("Enter username: ")
password = input("Enter password: ")

if users.get(username) == password:
    print("Welcome!")
else:
    print("Invalid credentials.")

#Exercise 7 — Contact Book
contacts = {
    "Nada": "0612345678",
    "Youssef": "0698765432"
}

name = input("Enter contact name: ")

phone = contacts.get(name)

if phone:
    print("Phone number:", phone)
else:
    print("Contact not found")

#Exercise 8 — Stock / Inventory Manager
inventory = {
    "coffee": 10,
    "tea": 5,
    "sandwich": 7
}

product = input("Enter product name: ")
quantity = int(input("Enter quantity to buy: "))

if product in inventory:
    if inventory[product] >= quantity:
        inventory[product] -= quantity
        print("Purchase confirmed!")
        print("Remaining stock:", inventory[product])
    else:
        print("Error: Insufficient stock.")
else:
    print("Error: Product does not exist.")

#Exercise 9 — Website Analytics Counter
visits = {
    "homepage": 1200,
    "courses": 350,
    "contact": 90
}

page = input("Which page was visited? ")

if page in visits:
    visits[page] += 1
    print("Page updated")
    print("New visit count:", visits[page])
else:
    print("Error: Page does not exist in analytics system.")