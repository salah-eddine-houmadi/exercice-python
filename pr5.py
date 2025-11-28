# #pr

email = input("Enter your email address: ")

domain = email.split('@')[1]

print("Domain:", domain)

# #pr

review = input("Enter the customer review: ")

word_to_count = "quality"
count = review.lower().split().count(word_to_count)

print(f"The word '{word_to_count}' appears {count} times.")

# #pr
items = [("Laptop", 1200.99), ("Mouse", 25.50)]

print(f"{'Item':<10} {'Price':>10}")
print("-" * 20)

for item, price in items:
    print(f"{item:<10} ${price:>9.2f}")

# #pr
sentence = "Lkhibra Academy is great"

reversed_sentence = " ".join(sentence.split()[::-1])

print(reversed_sentence)

# #pr
import re

text = "Loving #Python and #Coding at #LkhibraAcademy"


hashtags = re.findall(r"#\w+", text)

print("Hashtags:", hashtags)

#pr

import re

password = input("Enter password: ")

has_length = len(password) >= 8
has_number = re.search(r"\d", password)
has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

if has_length and has_number and has_special:
    print("Strong password")
else:
    print("Weak password")

#pr

text = "  Hello   World   !  "
cleaned = " ".join(text.split())
print(cleaned)

#pr

text = "lkhibra academy python training"
title_case = text.title()
print(title_case)

#pr

text = "I love Python programming"
updated = text.replace("Python", "Java")
print(updated)