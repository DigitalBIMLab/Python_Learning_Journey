# Python_Learning_Journey
My Python learning journey,documenting notes, practicing concepts, and building projects from scratch.
Author - Ar.Dk
'''VARIABLE'''
x = 4
y = 5
print(sum(x+y))    #This produces a TypeError because x + y equals 30, an integer, and sum() expects an iterable such as a list.
print("SUM:",x+y)


'''Strings''' #Immutable
str_01 = 'HI'
str_02 = "Hello World"
str_03 = '''Deepak'''
print("Hello Deepak\nLets Start.")

#concartenation
str_01 = "Deepak"
str_02 = "Kumar"
print(str_01+str_02)    #DeepakKumar
print(str_01,str_02)    #Deepak Kumar

#Indexing
Name = "DEEPAK KUMAR BISWAS"
print(Name[3])  
Name[3]= "New Name" 
#Index Form can't change the characters.

#Slicing
str[starting_idx : ending_idx]    ending idx is not included.
Name = "1234567890abcx"
print(Name[2 : 7])  #34567
print(Name[  : 4])  #1234       starting & ending idx is default.
print(Name[7 :  ])  #890abcx    starting & ending idx is default.
print(Name[-4:-1])  #abc        (-) counts from ending to start.

'''Function'''
name = "Deepak Kumar biswas" 
print(name.endswith("a"))               #false
print(name.replace("Deepak", "dstar"))  #dstar Kumar biswas

#list of String Methods
str_name.upper()        Converts text to uppercase
str_name.lower()        Converts text to lowercase
str_name.title()        Capitalizes each word
str_name.capitalize()	  Capitalizes the first character
str_name.strip()        Removes leading/trailing whitespace
str_name.replace()      Replaces part of a string
str_name.split()        Splits a string into a list
str_name.join()         Joins strings together
str_name.find()         Finds a substrings position
str_name.count()        Counts occurrences
str_name.startswith()	  Checks the beginning of a string
str_name.endswith()     Checks the end of a string
str_name.isdigit()      Checks whether all characters are digits
str_name.isalpha()      Checks whether all characters are letters
str_name.format()       Formats a string
str_name.casefold()	    Normalizes text for case-insensitive comparison



'''Conditional Statements'''
if condition_01:
    Statement_01 
elif condition_02:
    Statement_02
 else:
    Statement_03

x = 17
if x>=18:
     print("YOU ARE AN ADULT")
elif x<17 or x>=16: #we use "and" when whant both the condition true.
     print("PLEASE APPLY FOR YOUR VOTER CAD")
else:
     print("YOU ARE NOT ADULT")

'''LIST''' #Mutable
marks = [90, 24, 50 , 30 , 65, 99, 13]
MARKS = [] EMEPTY LIST,ITS ALSO VALID
print(marks[3])     #30
marks[3] = 55
print(marks)        #[90, 24, 50, 55, 65, 99, 13]

'''LIST METHODS'''
str_name.append()     Adds one item at last
str_name.extend()	    Adds multiple items
str_name.insert()	    Inserts an item at a position
str_name.remove()	    Removes an item by value
str_name.pop()        Removes and returns an item
str_name.clear()	    Removes all items
str_name.sort()       Sorts the list in place
str_name.reverse()	Reverses the list in place
str_name.index()	    Finds an items index
str_name.count()	    Counts occurrences
str_name.copy()       Creates a shallow copy
str_name.sort)        arraging in accending oder.

marks.extend([40, 50, 60])      
# () Call a function or method and pass arguments.
# [] Create a list or access list elements.
print(marks)

'''TUPLES''' #IMMUTABLE
MARKS = () EMEPTY TUPLE,ITS ALSO VALID
marks = (90, 24, 50 , 90, 75, 90,  30 , 65, 99, 13)
marks = (90,)       #To tell python its a tuple use (,) at the ends of single value.
print(type(marks))  #<class 'tuple'>

'''TUPLE METHODS'''
str_name.index(el)      returens the index number of the first occurrences.
str_name.count(el)      Count the total occurrences.

print(marks.count(90))    #3
print(marks.index(50))    #2


'''DICTIONARIES'''
# info = keys : value,    
#need to add , at the end.
#need to add : to assign value to key.
# info={}  # empty Dict
info = {
     "Name":"Deepak Kumar",              
     "Class":"1st",
     "Roll N0.":19145,
     "address":"Chandangarh Ward N0.3",
     "Subjects":["Physics", "Chemistry", "math"]
}
print(info)

'''DICTIONARIES METHODS'''
Dic_name.keys()	          Gets dictionary keys
Dic_name.values()	        Gets dictionary values
Dic_name.items()	         Gets key-value pairs
Dic_name.get()	           Gets a value safely using a key
Dic_name.update()	        Updates dictionary entries
Dic_name.pop()	           Removes an entry and returns its value
Dic_name.popitem()	       Removes and returns the last inserted pair
Dic_name.setdefault()	    Gets a value or inserts a default
Dic_name.clear()	         Removes all entries
Dic_name.copy()	          Creates a shallow copy
Dic_name.update(New_Dict) Insert the items of New_Dict into the Dictionary.

print(info.items())
print(info.get("Roll N0."))     #this method didn't give us error instred it give us none for invalid input.


'''SETS'''#IMMUTABLE
nums = set()  ,emepty set
nums = {1, 2, 3, 4}
set_02 = {1,2,2,3,4}
print(nums)
print(set_02)

'''SETS METHODS'''
set_name.add()            Adds an element
set_name.update()         Adds elements from an iterable
set_name.remove()         Removes an element; raises an error if absent
set_name.discard()        Removes an element if present
set_name.pop()            Removes and returns an arbitrary element
set_name.clear()          Removes all elements
set_name.union()          Combines sets
set_name.intersection()   Gets common elements
set_name.difference()     Gets elements in one set but not another
set_name.issubset()       Checks whether a set is a subset
set_name.issuperset()     Checks whether a set is a superset

nums = {1, 2, 3, 4}
nums.add(5)
print(nums)     #{1,2,3,4,5}

'''LOOPS'''
1. while loops
2. for loops

while loops
Count = 1
while Count <= 5:
    print("hello")
    Count +=1        #Count = Count+1
# We take small variables like  i,j,k,x,y etc.
i = 1
while i <= 5:
    print("hello")
    i +=1
    
i = 1
while i <=100:
    print(i)
    i+=1
print("END LOOP")

#Table of n
n = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(f"{n} X {i:<2} = {n * i}")
    i += 1

print("END LOOP")

'''f"{i:<2}"
i is the value you want to display.
2 reserves a field width of two characters.
< aligns the value to the left within that space.
'''
