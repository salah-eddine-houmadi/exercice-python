#Manage a Shopping Cart

shopping_cart = []

shopping_cart.append("Apples")
shopping_cart.append("Milk")
shopping_cart.append("Bread")

shopping_cart.remove("Milk")

shopping_cart.insert(0,"Eggs")

print(shopping_cart)

#Process High Scores

scores = [45,12,88,67]

scores.extend([95,74])

scores.sort(reverse=True)

top_scores = scores[:3]

print(top_scores)

#Combine Product Data

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [1200, 45, 80, 250]

for products, prices in zip(products,prices):
    print(f"Product : {products}, Price :{prices}")

#Enumerate a Guest List

guests = [" Alice", "Bob", "Charlie", "David", "Eve "]
vip_list = [" Charlie", "Eve "]

for number, guests in enumerate(guests, start=1):
    if guests in vip_list:
        print(f"check-in #{number}: {guests} (VIP)")
    else:
        print(f"check-in #{number} :{guests}")

#Filter Sales Data

sales = [35.50, 120.00, 80.25, 500.75, 45.00]

significant_sales = [sale for sale in sales if sale > 100]

print(significant_sales)