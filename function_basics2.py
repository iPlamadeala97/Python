#1: Countdown
#Create a function that accepts a number as an input. 
#Return a new list that counts down by one, from 
#the number (as the 0th element) down to 0 (as the last element).
def countdown(number):
    new_list = []
    for i in range(number, -1, -1):
        new_list.append(i)
    return new_list

print(countdown(5))

#2: Print and Return
#Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
def list_function(list):
    print(list[0])
    return list[1]

print(list_function([1,2]))

#3: First Plus Length
#Create a function that accepts a list and returns the sum of 
#the first value in the list plus the list's length.
def first_plus_length(list):
    print(list[0])
    return len(list)

my_list = [1, 2, 3, 4, 5]
print(first_plus_length(my_list))

#4: Values Greater Than Second
#Write a function that accepts a list and creates a new list 
#containing only the values from the original list that are 
# greater than its 2nd value. Print how many values this is 
#and then return the new list. If the list has less than 2 elements, 
#have the function return False
def values_greater(list):
    if len(list) < 2:
        return False
    new_list = []
    for x in list:              # for x in range(len(list)): didn't work     
        if x > list[1]:
            new_list.append(x)
    print(len(new_list))
    return new_list

my_list = [4, 2, 5, 7, 8]      
print(values_greater(my_list))                      

#5: This Length, That Value
#Write a function that accepts two integers as parameters: size and value. 
#The function should create and return a list whose length is equal 
#to the given size, and whose values are all the given value.#

def this_length(size, value):
    new_list = []
    for x in range(size):
        new_list.append(value)
    return new_list

print(this_length(5, 10))