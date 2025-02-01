#STRING SLICING:

#A string in python can be sliced for getting a part of the strings.
#String are immutable, once we declare then we can not change it.

#EXAMPLE:

Name = "Divakar" # Length=7 

#Positive Index--->0 1 2 3 4 5 6
#                  D i v a k a r
#---------------------------------------------------------------------------------------------------------------
#                   D  i  v  a  k  a  r
#Negative Index--->-7 -6 -5 -4 -3 -2 -1

#The index in a sting starts from 0 to (length -1) in Python. In order to slice a string we use following syntax.

#Syntax :
 
# slice = Name[starting_index : Ending_Index]
# NOTE: 1.starting_index is included 
#       2.Ending_Index is not included


slice = Name[0:7]
print(slice) # It will print "Divakar"
slice = Name[0:6]
print(slice) # It will print "Divaka"
slice = Name[2:5]
print(slice) # It will print "vak"
slice = Name[:7]
print(slice) # print "Divakar", Because Name[:7] it means [all the characters in left side: end character]
slice = Name[0:]
print(slice) # printing "Divakar", Because Name[0:] it means [index 0 :all the characters in rigth side]

#---------------------------------------------------------------------------------------------------------------

#Negative Indices: Negative indices can also be used as shown in the figure above. -1 corresponds to the (length - 1) index, -2 to (length - 2).

slice = Name[::-1]
print(slice) # it will print reverse order "rakaviD"
slice = Name[1]
print(slice) # it will print "r"
slice = Name[-4:-2]
print(slice) #it's going to print "ak"
#----------------------------------------------------------------------------

#SLICING WITH SKIP VALUE:

# We can provide a skip value as a part of our slice like this:

Word = "Fantastic"
Skip_Slicing = Word[0:5:2] # That is [starting_index:Ending_index:Number_of_Skip (or) next number to pick]
print(Skip_Slicing) # printing like this 
alphabets = 'abcdefghijklmnopqrstuvwxyz'
slice = alphabets[1:10:3]  
print(slice)