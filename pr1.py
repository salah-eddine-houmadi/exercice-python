#pr

name = "Alex"
number = 30
course = "Python"

print(f"The instructor is {name}, there are {number} in the {course} class!")

#pr

students_morning = 15
students_evening = 25

print(f"Before Swap: Morning Batch = {students_morning}, Evening Batch {students_evening}")
students_morning, students_evening = students_evening, students_morning

print(f"After Swap: Morning Batch = {students_morning}, Evening Batch {students_evening}")

#pr
python = 25
java = 18
ai = 12

print(f"Python = {python}, Java = {java} , AI = {ai}")

#pr
age = 21
course_rating = 4.9
course_name = "Python"

print(f"{age} is of type {type(age)}")
print(f"{course_rating} is of type {type(course_rating)}")
print(f"{course_name} is of type {type(course_name)}")

#pr

instructor = "The instrucor"
academy = "Lkhibra Academy"
slogan = "Learing Python is fun!"

print(f"{instructor} at {academy} says: \"{slogan}\" ")

#pr

integer_valeur = 100
string_value ="42"

print(f"Integer value :{integer_valeur}, Type:{type(integer_valeur)}")
print(f"String value :{string_value}, Type:{type(string_value)}")

#pr

number_1 = 9.75
number_2 = 50

number_3 = int(number_1)
number_4 = float(number_2)

print(f"Float to Int : {number_3}, Type:{type(number_3)}")
print(f"Int to Float : {number_4}, Type:{type(number_4)}")

#pr

number_1 = True
number_2 = False

number_3 = int(number_1)
number_4 = int(number_2)

print(f"True as an integer: {number_3}")
print(f"False as an integer: {number_4}")

#pr

course_1 = "Python"
course_2 = "is"
course_3 = "amazing"

print(f"List to String :{course_1}, {course_2} ,{course_3}")
print(f"String to List :[{course_1}, {course_2} ,{course_3}]")

courses = ["Python", "is", "amazing"]


list = ",".join(courses)

string = list.split(",")

print(f"List to String: {list}")
print(f"String to List: {string}")

#pr

my_dict = {
    "name": "Lkhibra Academy",
    "age": 5,
    "language": "Python"
}

keys_list = [key for key in my_dict.keys()]
values_list = [value for value in my_dict.values()]

print(f"Keys: {keys_list}")
print(f"Values: {values_list}")


#pr

a = 10
b = 5 

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")

#pr

a = 10
b = 5


print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} == {a}: {a == a}")
print(f"{a} != {b}: {a != b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

#pr

a = True
b = False

# Logical operations
and_result = a and b
or_result = a or b
not_result = not a

# Print results
print(f"True and False: {and_result}")
print(f"True or False: {or_result}")
print(f"Not True: {not_result}")


#pr
x = 10
print(f"Initial Value: {x}")


x += 5
print(f"After += : {x}")

x -= 3
print(f"After -= : {x}")

x *= 2
print(f"After *= : {x}")

x /= 3
print(f"After /= : {x}")

x %= 8
print(f"After %= : {x}")

#pr


a = 5
b = 3


and_result = a & b
or_result = a | b
xor_result = a ^ b
left_shift = a << 1
right_shift = a >> 1


print(f"{a} & {b} = {and_result}")
print(f"{a} | {b} = {or_result}")
print(f"{a} ^ {b} = {xor_result}")
print(f"{a} << 1 = {left_shift}")
print(f"{a} >> 1 = {right_shift}")