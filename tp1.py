#pr Variable Assignment

frined = input("you friend type in :")

print(f"hello, {frined}! Welcome.")

#pr Tip Calculator

mealCost = float(input("Cost of the meal:"))
taxRate = float(input("Tax rate(%):"))
tipPercentage = float(input("Tip (%):"))

totalcost = mealCost +(mealCost * (taxRate/100)) + (mealCost * (tipPercentage/100))

print(f"The total cost, including tax and tip, is ${totalcost:.2f}.")

#pr Road Trip Planner


kilomter= float(input("Enter distance in kilometers:"))

mile = kilomter * 0.621371

print(f"Hey! That's roughly {mile:.4f} miles away.")


#pr Area of a Triangle

base = float(input("The base of the triangle :"))
height = float(input("Height of the triangle:"))

area = 1 / 2 * base * height

print(f"The area of the triangle is {area} square units.")


#pr Basic Calculator (Part 1)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

additon = num1 + num2
subtration = num1 - num2
multipliction = num1 * num2

if num2 != 0:
    division = num1 / num2
else :
    division = "undefined (cannot divide by zero)"

print(f"{num1} + {num2} = {additon}")
print(f"{num1} - {num2} = {subtration}")
print(f"{num1} * {num2} = {multipliction}")
print(f"{num1} / {num2} = {division}")