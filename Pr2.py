# STUDENT ID: 20CE065
# STUDENT NAME: SHRUTI PAGHADAL
# AIM: Study and Learn List, Tuple, Set and Dictionary 
# GITHUB LINK: https://github.com/Shruti423/Practical_2.git

print("------------------------------------------- DICTIONARY ------------------------------------------------")
print("--------------------- TASK 1 OF DICTIONARY --------------------------")
# TO CHECK WHETHER THE GIVEN KEY ALREADY EXISTS IN THE DICTIONARY OR NOT
dict1={"a":"shruti","b":"paghadal","c":"charusat","d":"cspit"}
def is_key_present(y):
    if y in dict1:
        print(y,"is present in the dictionary")
    else:
        print(y,"is not present in the dictionary")
is_key_present("d")
is_key_present("f")

print("--------------------- TASK 2 OF DICTIONARY --------------------------")
# TO MERGE TWO PYTHON DICTIONARIES
dict2={"e":"ce","f":"python"}
print("DICTIONARY 1 is: ", dict1)
print("DICTIONARY 2 is: ", dict2)
def Merge(dict1,dict2):
    return(dict1.update(dict2))
print(Merge(dict1,dict2)) # this returns None
print("After merging Dictionary 1 & Dictionary 2, the final dictionary is:",dict1) # changes are made in dict1 and prints the merged dictionary

print("--------------------- TASK 3 OF DICTIONARY --------------------------")
# TO SUM ALL THE ITEMS IN A DICTIONARY
def returnSum(myDict): # function to add all items in a dictionary
    lst=[]
    for i in myDict:
        lst.append(myDict[i])
    final=sum(lst)
    return final
dict3={"x":100,"y":200,"z":300}
print("Dictionary 3 is:",dict3)
print("Sum of all the items in Dictionary 3 is:",returnSum(dict3))

print("--------------------- TASK 4 OF DICTIONARY --------------------------")
# ADDING A NEW KEY TO THE DICTIONARY 
sample1={0:10, 1:20}
print("Current Dictionary is:",sample1)
sample1[2]=30
print("Updated Dictionary after adding new key is:", sample1) # prints the updated dictionary after adding new key

print("--------------------- TASK 5 OF DICTIONARY --------------------------")
# CONCATING GIVEN DICTIONARIES TO CREATE A NEW ONE
dic1={1:10,2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic4={}
print("DICTIONARY 1:",dic1)
print("DICTIONARY 2:",dic2)
print("DICTIONARY 3:",dic3)
for d in (dic1,dic2,dic3): dic4.update(d)
print("AFTER CONCATENATION:",dic4)



print("--------------------------------------------- TUPLE -------------------------------------------------")
print("---------------------------- TASK 1 OF TUPLES ----------------------------------")
# CREATING A TUPLE WITH DIFFERENT DATATYPES
tuple1=("Tuple",True,2.0,2) # defined a tuple with string, boolean, float and integer as its datatypes
print("Tuple with different datatypes is:",tuple1)

print("---------------------------- TASK 2 OF TUPLES ----------------------------------")
# CREATING A TUPLE WITH NUMBERS AND PRINTING ONE ITEM
tuple2=5,10,15,20,25 # created a tuple with numbers
print("Tuple is:",tuple1)
tuple2=5, #printing one item
print("Printing one item of the tuple:",tuple2)

print("---------------------------- TASK 3 OF TUPLES ----------------------------------")
# TO ADD AN ITEM IN A TUPLE
tuple3=(1,2,3,4,5,6,7) # create a tuple
print("The tuple is:",tuple3)
lst=list(tuple3) # converting tuple to list
lst.append(8)
tuple3=tuple(lst) # converting list back to tuple
print("after adding an item to the existing tuple:",tuple3)

print("---------------------------- TASK 4 OF TUPLES ----------------------------------")
# CONVERTING TUPLE TO A STRING
def convertTuple(tup):
    str='' # define an empty string
    for item in tup:
        str=str+item
    return str
tuple4=('s','h','r','u','t','i')
print("the tuple is:",tuple4)
str=convertTuple(tuple4)
print("after conversion to string:",str)

print("---------------------------- TASK 5 OF TUPLES ----------------------------------")
# TO FIND THE LENGTH OF THE TUPLE
tuple5= tuple("CHARUSAT")
print("the tuple is:",tuple5)
print("the length of the tuple is:", len(tuple5)) # using the len() function to know the length

print("------------------------------------------------ SET -------------------------------------------------------")
print("------------------------------- TASK 1 OF SETS -------------------------------------")
# ADDING AN ITEM AND CLEARING THE SET AFTERWARDS
set1=set()
print("Set1 is:",set1)
set1.update(["Shruti","Python","Sets"]) # adding items
print("After adding items in set:",set1)
set1.clear() # clearing the set
print("after clearing the set:", set1)

print("------------------------------- TASK 2 OF SETS -------------------------------------")
# REMOVE AN ITEM FROM SET IF IT IS PRESENT IN IT
set2= set(["banana","apple","cherry","strawberry"])
print("the original set is:",set2)
def Remove (set2):  # removes an item from the set
    set2.remove("apple")
    print("After removing an item:",set2)
Remove(set2)

print("------------------------------- TASK 3 OF SETS -------------------------------------")
# CREATING AN INTERSECTION, UNION AND DIFFERENCE OF SETS
set3={10,20,30}
set4={30,40,10}
print("Set 3 is:",set3)
print("set 4 is:",set4)
print("The difference of sets (set 3 - set 4): ", set3.difference(set4))
print("The intersection of set 3 and set 4 is: ", set3.intersection(set4))
print("The union of set 3 and set 4 is: ", set3.union(set4))

print("------------------------------- TASK 4 OF SETS -------------------------------------")
# TO FIND THE MINIMUM AND MAXIMUM VALUE IN A GIVEN SET
set5={5,10,3,15,2,20}
print("the original set is:", set5)
print("the maximum value in the set is:",max(set5))
print("the minimum value in the set is:",min(set5))

print("------------------------------- TASK 5 OF SETS -------------------------------------")
# FINDING THE MOST COMMON ELEMENT AND THEIR COUNTS IN LIST, TUPLE, DICTIONARY
# IN LIST
print("-------------------------- SUB PART (A) OF TASK 5 -----------------------------------")
list_of_words=["cats","dogs","snakes","cats","cats","cats","flowers"]
print("the original list of items is:",list_of_words)
from collections import Counter
count=Counter(list_of_words)
count.most_common(1)
print("The most common element and the count in list is:",count.most_common(1))

# IN TUPLE
print("-------------------------- SUB PART (B) OF TASK 5 -----------------------------------")
tuple_of_words=('cakes','cookies','biscuits','cakes')
print("the original tuple of items is:",tuple_of_words)
from collections import Counter
count1=Counter(tuple_of_words)
count1.most_common(1)
print("The most common element and the count in tuple is:",count1.most_common(1))

# IN DICTIONARY
print("-------------------------- SUB PART (C) OF TASK 5 -----------------------------------")
dict_of_words=['red','green','orange','black','red','red','red','white','black','red']
print("the original dictionary of items is:", dict_of_words)
from collections import Counter
count2=Counter(dict_of_words)
print("The most common element and the count in dictionary is:",count2.most_common(1))

