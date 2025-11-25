#pr

num = int(input("Enter a number: "))


if num % 2 == 0:
    print(f"{num} even number")
else:
    print(f"{num} odd number")

#pr

a, b, c = map(int, input("enter number: ").split())

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("largest number  :", largest)

#pr

year = int(input("enter year :"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#pr

N = int(input("enter number :"))

for i in range(1,N +1):
    print(i)

#pr

N = int(input("enter number :"))

for i in range(1,N+1):
        if i % 2 == 0:
            print(i)

#pr

N = int(input("enter number :"))

total = 0

for i in range(1,N +1):
    total += i
print("sum ", N , "is", total)
    
#pr

N = int(input("enter number :"))
    
factorial = 1

for i in range(1,N + 1):
    factorial *= i

print(f"factorial {N} is {factorial}")


#pr

num = int(input("Enter a number: "))

reversed_num = 0

while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10

print(" number:", reversed_num)

#pr

N = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{N} x {i} = {N * i}")

#pr

num = int(input("enter a number "))

count = 0
temp = num

while temp != 0:
    temp = temp // 10
    count += 1

print(f"number {count}")

