#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1: Change the value 10 in x to 15. 
#Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x [1] [0] = 15

#1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students [0] ['last_name'] = 'Bryant'

#1.3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory ['soccer'] [0] = 'Andres'

#1.4 Change the value 20 in z to 30
z [0] ['y']= 30

#2 Iterate Through a List of Dictionaries 
#Create a function iterateDictionary(some_list) that, given a list of dictionaries,
#the function loops through each dictionary in the list and prints each key and the associated value.

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
    for dict_item in some_list:
        for key in dict_item:
            print dict_item[key]

iterateDictionary(students)

#3 Get Values from a List of Dictionaries 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name, some_list):
    return [student[key_name] for student in students]

print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))

#4 Iterate Through a Dictionary with List Values
#Create a function printInfo(some_dict) that given a 
#dictionary whose values are all lists, prints the name 
#of each key along with the size of its list, and then 
#prints the associated values within each key's list.
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(len(some_dict['locations']), "Locations")
    for location in some_dict['locations']:
        print(location)
    print(len(some_dict['instructors']), "Instructors")
    for instructor in some_dict['instructors']:
        print(instructor)

print(printInfo(dojo))