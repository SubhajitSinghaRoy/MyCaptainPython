# assignment one---1
# 1....
print("******************ASSIGNMENT 1**********************")
a = int(input("enter the first value\n"))
b = int(input("enter the second value\n"))
print("the sum of two values is:", a + b)
print("the difference of two values is:", a - b)
print("the multiplication of two values is:", a * b)
print("the division of two values is:", a / b)
print("the modulus(remainder) of two number is", a % b)
print()
# ---------------------------------------------------------

# 2....

# given: 10,1,8,3,6,5,4,x,y
# step 1:start
# step 2:x is the second last value
# step 3:x=2n-1
# step 4:y=n(2n-1)
# step 5:stop/end


# --------------------------------------------------------------
# assignment 1.2....
print("******************ASSIGNNMENT 1.2*******************")
a = int(input("enter the first value\n"))
b = int(input("enter the second value\n"))
if a > 0 and b > 0:
    print("The numbers a and b are greater than 0")
else:
    print("Atleast one number is not greater than 0")
a = int(input("enter the first value\n"))
b = int(input("enter the second value\n"))
if a > 0 or b > 0:
    print("either one number is not greater than 0")
else:
    print("both the numbers are greater than 0")

# ---------------------------------------------------------------------
# simple calculator using python
print("--------------------SIMPLE CALCULATOR----------------------")
print("*************************************************************")
while True:
    a = int(input("enter the first value\n"))
    b = int(input("enter the second value\n"))
    print("what do you want to do?")
    print("1. for addition 2. for subtraction 3. division 4.multiplication")
    choice = int(input("enter your choice\n"))
    if choice == 1:
        print("The value is:", a + b)
    if choice == 2:
        print("The value is:", a - b)
    if choice == 3:
        print("The value is:", a / b)
    if choice == 4:
        print("The value is:", a * b)
    print("do you want to quit this program:?(yes/no)")
    check = input(print("type 'yes' if you want to quit else type 'no'"))
    if check == "yes":
        break
    elif check =="no":
        continue
    else:
        print("THANK YOU FOR USING THE SIMPLE CALCULATOR")
    print("*******************************************************************")

# -----------------------------------------------------------------------------

# ***********Assignment 2.0*****************

# **********************Working with list.....*************************

list = [7, 1, 2, 6, 4, 47, 97]
print("printing original list: ")
# removing the item in a list
for i in list:
    print(i)
list.remove(6)
print("\nprinting the list after the removal of first element...")
for i in list:
    print(i)
# appending values in a list
print("list after appending the value is:")
list.append(30)
print("list after appending is:", list)
# finding the length of list
print("length of the list is:")
print(len(list))
# sorting of list
print("list after sorting")
list.sort()
print(list)
# inseting values at the specified position
list.insert(1, "45")
print("list afer inserting at the specified position is:")
print(list)

# ***************Working with dictionary********************

# dictionary example:
print("**************************WORKING WITH DICTIONARY *************************")
my_dict_1 = {1: 'apple', 2: 'ball', 3: 'car', 4: 'cat'}
my_dict_2 = {'name': 'rahul', 'age': 26, 'gender': 'male', 'hobby': 'dance'}
print("the dictionary is:", my_dict_2)

# accesiing the values in a dictionary


# Output: Jack from the dictionary made using the slice technique
print(my_dict_2['name'])

# Output: 26 which we get using the get() function
print(my_dict_2.get('age'))

# Changing and adding values in the given Dictionary
my_dict_2['age'] = 27
print("the updated dictionary after changing the value is:\n", my_dict_2)

# add item  into the dictionary
my_dict_2['address'] = 'delhi'
print("dictionary after adding the address item :")
print(my_dict_2)

# Get a list of the key:value pairs
x = my_dict_2.items()
print(x)

# removing the values in a dictionary
my_dict_2.pop("age")
print(my_dict_1)
print("the dictionary after removing the item is:", my_dict_2)

# Print all key names in the dictionary, one by one:
for y in my_dict_1:
    print(y)

# Print all values in the dictionary, one by one:
for z in my_dict_2:
    print(my_dict_2[z])

# Loop through both keys and values, by using the items() method:
for s, r in my_dict_1.items():
    print(s, r)

# Inserting an item to the dictionary:
my_dict_2.update({"status": "single"})
print(my_dict_2)

# ********STRING FUNCTIONS(WORKING WITH STRINGS)**********
print("************WORKING WITH STRINGS**********************")
str = "Hello"
str1 = " world"

#multiplication of strings
print(str * 3)

#concatenation of strings
print("concatenation of strings:",str + str1)

#string indexing:
print("string indexing :")
print(str[4])
print(str[2:4])

#checking in string if present or not present:
print('w' in str)
print('wo' not in str1)

#printing the string:
print(r'C://python37')
print("The string str : %s" % (str))

#string format
age = 12
txt = "My name is rahul, and I am {} years old"
print(txt.format(age))

#string methods
txt = input("enter the string in lower case so the result will be capitalized")
cap = txt.capitalize()
print (cap)

#ssting to lower
txt = input("enter the string in upper case to get the result in lower case...")
low= txt.lower()
print(low)

#string to upper
txt = input("enter the string in lower case so the result will be in upper case")
up= txt.upper()
print(up)


#****************************THANK YOU***************************************************************

