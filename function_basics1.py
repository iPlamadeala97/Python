#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#predicted output: 5
#actual output: 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#predicted output: 5
#actual output: error, the number function is not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#predicted output:5
#actual output: same

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#predicted output: 5, 10
#actual output: 5; remember that the return keyword stops function execution so you exit out

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#predicted output: 5, 5
#actual output: 5, None; Hm, I think it's because since this is a new code block, the function has no parameters
#and no arguments are given. The print(5) is irrelevant to the x variable.

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#predicted output: 3, 5, 8
#actual output: 3, 5; Not exactly sure why the 8 isn't printed and why it shows up as NoneType.

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#predicted output:'2 5'
#actual output: 25 (removed single quotes and no space specified)

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#predicted output: 100, 10
#actual output: same

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#predicted output: 7, 14, 21
#actual output: same

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#predicted output: 8
#actual output: same

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#predicted output: 500, 500, 300, 500
#actual output: same

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#predicted output: 500, 500, 300, 300, 500
#actual output: 500, 500, 300, 500 (not twoo 300's)

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#predicted output: 500, 500, 500, 500
#actual output: 500 500 300 300 (I was wrong about what happens once inside the function;
# I thought b with value of 500 is put in as an argument and that this would change the value of b 
# inside of the function from 300 to 500. Turns out it doesn't change.)

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#predicted output: 1, 2
#actual output: 1, 3, 2 (I didn't think it would print the 3 because I thought that since the bar function
# is lower than the call it wouldn't recognize it, but I forgot that it already read the bar function
# declaration and then once inside the foo function it reads the bar function call.)

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#predicted output: 1, 3, 5, 10
##actual output: same