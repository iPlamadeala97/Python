num1 = 42       
#variable declaration with value of 42
num2 = 2.3
#variable declaration with value of 2.3
boolean = True
#Boolean declaration of Boolean with value of True
string = 'Hello World'
#string declaration with value of "Hello World"
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#variable declared and list created with list items 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#variable declared and list created with tuples (?)
fruit = ('blueberry', 'strawberry', 'banana')
#variable declared and list created with list itse (not sure the difference 
#betweeen this one with parenthesese and the one on line 9 with brackets)
print(type(fruit))
#print command calling the function type() with value of fruit
print(pizza_toppings[1])
#print command accessing the value in the first index of the list in the pizza_toppings function
pizza_toppings.append('Mushrooms')
#add value to the end of the pizza_toppings list
print(person['name'])
#print command calling the function person and the value stored in name
person['name'] = 'George'
#change value stored in name in the person list
person['eye_color'] = 'blue'
#add value in name
print(fruit[2])
#print command accessing the value in the second index of the fruit list

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#conditional with if, else

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#conditional with if, else if, else 

for x in range(5):
    print(x)
#for loop with start and stop of 5

for x in range(2,5):
    print(x)
#for loop with start of 2 and stop of 5

for x in range(2,10,3):
    print(x)
x = 0
#for loop with start of 2, stop of 10, and increment of 3

while(x < 5):
    print(x)
    x += 1
#while loop until x is no longer less than 5, incrementing by 1

pizza_toppings.pop()
#take out the last value in the pizza_toppings list
pizza_toppings.pop(1)
#take out the value in index 1 of the pizza_toppings list

print(person)
#print value(s) stored in the person function
person.pop('eye_color')
#take out the eye_color value/tuple in the person function
print(person)
#print value(s) stored in the person function

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#for loop with continue and print if first condition is met, then break
#if second condition is met

def print_hello_ten_times():
    for num in range(10):
        print('Hello')
#defines a function, print string the number of times specified in the range

print_hello_ten_times()
#defines a function, but the function has no arguments

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
#defines a function, print string the number of times equal to the value of x

print_hello_x_times(4)
#Error; this is calling the function, but it hasn't been declared or defined yet

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
#defines a function, print string Hello the number of times equal to the value of x, 
#which is 10

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
#I think these are both errros; the functions are called without
#having been declared


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)