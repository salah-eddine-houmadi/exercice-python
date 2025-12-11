#The Coffee Machine Timer

import time

for s in range(10,0,-1):
    print(s)
    time.sleep(1)

print("Your coffee is ready!")

#Simple Investment Calculator

obj = 1000
rate = 0.05

for year in range(1,6):
    obj += obj * rate
    print(f"Year {year}: ${obj}")

#ATM PIN Validation

correct_pin ="1234"
pin = ""

while pin != correct_pin:
    pin = input("enter your pin :")

    if pin != correct_pin:
        print("the password is incorrect please try agai.")

print("the Pin is correct.")

#Factory Quality Control

for i in range(1,51):
    print(f"checking item {i}")

    if i % 7 == 0:
        print(f"i {i}")
        continue

    print(f"item {i} is OK.")

#Rocket Launch Simulator
    
fuel = 1000
altitude = 0

while fuel > 0:
    fuel -= 100
    altitude += 50

    print(f"Altitude: {altitude}, fuel: {fuel}")

    if altitude > 1500 and fuel < 200:
        print("Mission Aborted: Low fuel at critical altitude.")
        break
    if altitude >= 2000:
        print("Success! Stable orbit reached.")
        break

if fuel <= 0 and altitude < 2000:
    print("Mission Failed: Ran out of fuel.")