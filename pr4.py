
#pr

shopping = ["milk", "Eggs","Bread"]

shopping.append("Tomatos")

print(shopping)

#pr

scores = [88,92,75,100,89]
scores.sort()

print(scores)

#pr

prices =[299, 159, 499, 120, 349]
most_expensive = max(prices)

print(f"Most expensive product costs: {most_expensive}")

#pr

sentence = "Python is great and Python is fun"

words = sentence.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word,0) +1

print(word_count)

#pr
student = {
    "Sarah":"A"
}

print("Sarah 's grade:", student["Sarah"])

#pr
student_1 = {"Salah", "Alice", "David"}
student_2 = {"adil", "Alice", "David"}

both = student_1 & student_2

print(both)

#pr
text = "Python is amazing and Python is powerful"
unique = set(text.split())

print(unique)

#pr
menu = {
    "Burger": 9.99,
    "Pasta": 12.99,
    "Salad": 7.99,
    "Pizza": 14.99
}


print("Pasta costs:", menu["Pasta"])

#pr
inventory = {
    "Laptops": 15,
    "Monitors": 25,
    "Keyboards": 50,
    "Mice": 75
}


print("Laptops in stock:", inventory["Laptops"])

#pr

reviews = [
    "The product is excellent",
    "Excellent service and excellent quality",
    "I had an excellent experience"
]


words = " ".join(reviews).lower().split()


word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1


most_frequent = max(word_count, key=word_count.get)

print("Most frequent word:", most_frequent)


#pr
visitor_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.1", "192.168.1.3"]
unique_visitors = set(visitor_ips)


print("Unique visitors:", len(unique_visitors))

#pr
laptop_customers = {"John", "Sarah", "Alex", "Emma"}
monitor_customers = {"Alex", "David", "Sarah", "Mike"}


both_customers = laptop_customers & monitor_customers  

print("Customers who bought both:", both_customers)

#pr
registered_students = {"Ali", "Lina", "Omar", "Sara", "Nina"}
attended_students = {"Ali", "Sara", "Nina"}

absent_students = registered_students - attended_students  

print("Absent students:", absent_students)

#pr

stock1 = {"Laptops": 10, "Monitors": 5}
stock2 = {"Keyboards": 8, "Mice": 12}


merged_stock = stock1 | stock2

print(merged_stock)

#pr

product = [101, 102, 103, 101, 104, 102]
unique = list(set(product))

print("Unique product IDs:", unique)