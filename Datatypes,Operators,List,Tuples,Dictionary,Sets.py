# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 18:54:36 2021

@author: shivani arade
"""
'''variable names-case sensitive,start with letter,cannot start witn no. or _ and end with _'''

'''camel case-myVariableName(each word except 1st starts with capital letter)
pascal case-MyVariableName(each word starts with capital letter)
snake case-my_variable_name(each word separated by _)'''
#camel
ageEmp=45 #lower
AgeEmp=45 #upper
#snake
age_emp=45   #letter after the underscore small letter
Age_emp=45
#pascal
AgeEmp=45

#datatype
"""Data Types"""
'''text type=str'''
x="shivani"

'''numeric type=int float complex'''
'''no conversion of complex no'''    
x=20
x=20.5
x=1j

'''sequence type=list tuple range'''
x=["apple","banana","cherry"]     
x=("apple","banana","cherry")     
x=range(6)  
                    
'''mapping type=dict ''' 
x={"name":"John","age":"36"} 
  
'''Set type=set frozenset'''
x={"apple","banana","cherry"}
x=frozenset({"apple","banana","cherry"})

'''boolean type=bool'''
x=True

'''binary types=bytes bytearray memoryview'''
x=b"Hello"
x=bytearray(5)
x=memoryview(bytes(5))
print(x)

#
a=8
type(a)
b=4.5
type(b)
c="Shivani"
type(c)

#verify datatype
type(a) is int

#coerce to new datatype
d=float(a)
d

'''the value enclosed within quotes is string then conversions not possible'''

#operators
a = 21
b = 10
c = 0
"""Operands: a,b,c
Operators:
Arithmetic,Assignment,Comparison,Logical,Identity,Membership,Bitwise
Arithmetic Operators: +,-,*,/,**,//,%
"""
c = a + b
print("Line 1 - Value of c is",c)
c = a - b
print("Line 2 - Value of c is",c)
c = a * b     #multiplication
print("Line 3 - Value of c is",c)
c = a / b     #division
print("Line 4 - Value of c is",c)
c = a % b     #modulus
print("Line 5 - Value of c is",c)
c = a**b      #exponentiation
print("Line 6 - Value of c is","i.e the value of a^b",c)
c = a//b      #floor division
print("Line 7 - Value of c is",c)

#heirarchy of operators in decreasing order of precedence
#parentheses,exponent,Division,multiplication,Add and subtract,bitwise and &

#relational or Comparison
a = 21
b = 10
print(a>b)
print(a<b)
print(a<= b)
print(a >= b)
print(a==b)
print(a!=b)

#logical:and,or,not
print((a>b) or (a<b))   #when one of them is true returns true
print((a>b) and (a<b))  #both conditions satisfied then only true otherwise false
print(not (a==b))

#bitwise
a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101
c = 0

c = a & b # 12 = 0000 1100          #and(both bits are 1)
print("Line 1 - Value of c is",c)
c = a|b # 61 = 0011 1101            #or(one of two bits is 1)
print("Line 2 - Value of c is ",c)   
print((a>b) | (a==b)) 

'''list are ordered,changeable,allow duplicate values,square brackets'''
list1=['p','q','r','b','e']

#postive indexing starts from 0(left)
#negative indexing starts from -1(right)

#accessing components
#nested list
nestedlist=['s',"happy",[2,0,1,5],1,2.5]
#top level
print(nestedlist[3])
#sublevel
print(nestedlist[2][1])
print(nestedlist[1][4])

#modify components using index
employee_list=[[1,2,3,4],['Ram','Preethi','Sathish','John'],4]
#modify top level
employee_list[2]=5
print(employee_list)
#modify sublevel
employee_list[1][3]="Karan"
print(employee_list)

#modify components using append
employee_list[0].append(5)
employee_list[1].append('nirmal')

#modify components using insert(position,object)
employee_list[0].insert(0,6)

#remove elements(del,remove,pop)
'''del-removes at specified position
remove-removes first matching element
pop-displays and removes at specified position'''
del employee_list[2]

employee_list[1].remove("Ram")
mylist=['p','r','o','b','l','e','m']
mylist.remove('p')

employee_list[0].pop(4)

'''Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
round brackets'''
'''no change,add,remove '''

#access tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])      #5 is exclusive
len(thistuple)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

'''Dictionaries=curly,key-value pair,ordered,changeable,no duplicates'''

#indexing not possible bcoz values are saved as key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#access(by key names)
x=thisdict["model"]
print(x)

#using get for values
x=thisdict.get("model")
print(x)

#getting keys and values annd items
x=thisdict.keys()
print(x)
x=thisdict.values()
print(x)
x=thisdict.items()
print(x)

#modify
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#modify using update
thisdict.update({"year": 2020})

#modify using del
del thisdict["year"]

#modify using clear
thisdict.clear()

'''Sets:unordered,unindexed,curly bracket,no duplicates'''
#add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#modify using discard
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
'''If the item to remove does not exist, discard() will not raise an error.'''

#clear set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#add elements from another set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#intersection()=return a new set that contains only items present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.intersection(y)
print(z)

'''difference()	Returns a set containing the difference between two or more sets'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.difference(y)
print(z)

#symmetric_difference()=return a new set that contains only items not present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.symmetric_difference(y)
print(z)























