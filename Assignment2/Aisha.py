A = 'A'
I = 'I'
S = 'S'
H = 'H'
A = 'A'

aX = 'A'

print(A)
print(I)
print(S)
print(H)
print(aX)

# Yes, variables show up on the variable editor

print(A, aX)

# No, there is no problem with two variables having the same character

aX = 'z'

print(A)
print(I)
print(S)
print(H)
print(aX)

# No, changing aX did not change the value of the other variables

aX = A

print(aX, A)

A = 'z'

print(aX, A)

# yes, changing the variable assignment changed the 'A' to 'z'. Therefore python variable assignment can change based on how it's defined
import numpy as np

# Operation Exercise

print(5/2)
print(5.0/2.0)

print(5 % 2) # gets remainder

print(5 ** 2) # exponent
print(5 // 2) # division without remainder

print(1+5+3*4/2) # BEDMAS order



# Boolean exercises

print(1 == 1.0) # equal
print("1" == "1.0") # not equal

print((3+2) == 5) # equal



# List exercises

oddlist = [1,3,5,7,9] # oddlist is a variable

print(oddlist) # prints same as oddlist

print(len(oddlist)) # prints 5

print(type(oddlist)) # prints <class 'list'>

intlist = list(range(0,100)) # prints all numbers between 0, 100

print(intlist)


# Dictionary exercises

about_me = {"name": "Aisha", "age": 22.0, "year_of_study": 4, "fav_food": ["roti", "daal", "paneer", "saag"]}

print(about_me)
print(type(about_me["name"])) # <class 'str'>
print(type(about_me["age"])) # <class 'float'>
print(type(about_me["year_of_study"])) # <class 'int'>
print(type(about_me["fav_food"])) # <class 'list'>

print(len(about_me)) # length is 4 determined by key value pairs



# Array exercises 

mixnums = [1,2,3,1.0,2.0,3.0]
print(mixnums) # array stays the same as definition

mixtypes = [1,2,1.0,2.0,"1","2"]
print(mixtypes) # array stays the same as definition

oddarray = list(range(1, 100, 2 ))
print(oddarray)

logarray = np.logspace(0,0.699,16)

print (logarray)
