# # Lists are used to store multiple items in a single variable.
list = ["Hi I am", "Divakar", 23, "Years", "Old","DOB is", 12.12]
print(list)
# # OUTPUT: ["Hi I am", "Divakar", 23, "Years", "Old","DOB is", 12.12]


# #List are mutable, List items are ordered, changeable, and allow duplicate values.
list[5] = "Date of Birth"
print(list)
# # OUTPUT: ["Hi I am", "Divakar", 23, "Years", "Old", "Date of Birth", "12.12"]


# # Python - Access List Items
# # List items are indexed and you can access them by referring to the index number:
# # EXAMPLE:
print(list[1]) # Output is "Divakar"


# # Negative Indexing
# # Negative indexing means start from the end, -1 refers to the last item, -2 refers to the second last item etc.
# # EXAMPLE:
print(list[-1]) #Output is "12.12"


# # Range of Indexes
# # You can specify a range of indexes by specifying where to start and where to end the range.
# # When specifying a range, the return value will be a new list with the specified items.
# # EXAMPLE:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# # OUTPUT : new list will be ["cherry","orange","kiwi"]
# # NOTE: The search will start at index 2 (included) and end at index 5 (not included).
# # Remember that the first item has index 0. because list index is start from 0.


# # By leaving out the start value, the range will start at the first item:
# # This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# # OUTPUT: ["apple","banana","cherry","orange"]


# # By leaving out the end value, the range will go on to the end of the list:
# # This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# # OUTPUT: ["cherry","orange","kiwi","melon","mango"]

# # Range of Negative Indexes
# # Specify negative indexes if you want to start the search from the end of the list:
# # This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# # OUTPUT:["orange","kiwi","melon"]


# # Check if Item Exists
# # To determine if a specified item is present in a list use the "in" keyword:
# # Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "Thanga Maari" in thislist:
  print("YES")
else:
  print("NO!")
#   # OUTPUT:NO!


# # Change Item Value
# # To change the value of a specific item, refer to the index number:
# # Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# # Output : ["apple","blackcurrant","cherry"]
# # NOTE: we can change the List item because list are "mutable" in python. 

# # Change a Range of Item Values
# # To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
# # Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# # OUTPUT: ["appale","blackcurrent","watermelon","orange","kiwi","mango"]

# # Insert Items
# # To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# # The insert() method inserts an item at the specified index:
# # Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"] 
thislist.insert(2, "watermelon")
print(thislist)
print(len(thislist))
# # NOTE: As a result of the example above, the list will now contain 4 items.
name = ["Divakar","Veeraj","Sam"]
name.insert(1, "Namratha")
print(name)


# # Append Items:
# # To add an item to the end of the list, use the append() method:
# # Using the append() method to add an item:
myList = ["A","B","C"]
myList.append("D")
print(myList)
# # NOTE: the append will add the item at last index.


# Extend List
# To append elements from another list to the current list, use the extend() method.
# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove Specified Item
# The remove() method removes the specified item.
# Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# NOTE:If there are more than one item with the specified value, the remove() method removes the first occurrence:

# Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index

# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist["banana"]
print(thislist)

# The del keyword can also delete the list completely.
# Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)


# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# Python - Sort Lists
# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# Use the copy() method
# You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Use the list() method
# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Python - Join Lists
# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
# Join two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:
# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


