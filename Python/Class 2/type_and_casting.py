#TYPE() FUNCTION :type() function is used to find the data type of a given variable in python.

x = 20 #int
print(type(x))

x = 20.2 #float
print(type(x))

x = 1j #complex
print(type(x))

x = "Sardar" #String
print(type(x))

x = [1,2,3,4,5,6,7,8,9] #List
print(type(x))

x = (1,2,3,4,5,6,7,8,9) #Tuple
print(type(x))

x = {"Name": "Divakar","Age" : 23} #dict
print(type(x))

x = {"Apple","Banana","Orange"} #set
print(type(x))

x = True #Boolean
print(type(x))

x = False #Boolean
print(type(x))

x = b'hello' #bytes
print(type(x))

x=frozenset({"APPLE", "ORGANGE", "BANANA"}) #frozenset
print(type(x))
#------------------------------------------------------------------------------------------

# TYPECASTING : Type casting, also known as type conversion, is the process of changing a variable's data type to another. It's an important feature in Python that allows for flexible operations and data manipulation. 

a = 10 
print(str(a)) # Converting integer to String type

b = "12"
print(int(b)) # Converting String to integer type

c = 16 
print(float(c)) # Converting integer to Float type

