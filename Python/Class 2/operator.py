# OPERATORS IN PYTHON

#Following are some common operators in python:

# 1. Arithmetic operators: +, -, *, **,/,/ etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc.
# 4. Logical operators: and, or, not.
#------------------------------------------------------------------------------------------

# 1. Arithmetic operators: Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division

#EXAMPLE: 
print("Addition",7+3)  # Here, 7 and 3 are the Operand, "+" is the operator. 7 + 3 = 10, final 10 this Result 

#Same as 
print("Subtraction:",7-3) # Subtraction
print("Multiplication:",7*3) # Multiplication
print("Division:",7/3) # Division
print("Modulus:",7%3) # Modulus 
print("Square root:",7**3) # Square root 
print("floor division:",(7//3)) #Floor Division :  floor division is a mathematical operation that rounds the result of a division down to the nearest whole number.
#------------------------------------------------------------------------------------------

# 2. Assignment operators: Assignment operators assign values to variables in programming languages. The left side of the operator is a variable, and the right side is the value to be assigned. 

#EXAMPLE:

a = 10    # Here, "=" is assigning the value to a variable 
a-= 5     # a-=5 means a = a - 5, That is a = 10 - 5 = 5
a+= 5     # a+=5 means a = a + 5, That is a = 5 + 5 = 10
print("value of a is: ",a)  # printing value of a  
#------------------------------------------------------------------------------------------

# 3. Comparison operators: Comparison operators compare values and return a true or false result. They are also known as relational operators. 

# == Equal to
# != Not equal to
# >  Greater than
# >= Greater than or equal to
# <  Less than
# <= Less than or equal to

#Example
x = 10
y = 10
print(x == y) 
print(x != y) 
print(x > y) 
print(x >= y) 
print(x < y) 
print(x <= y) 
#------------------------------------------------------------------------------------------

# Logical operators: Logical operators are used to compare two values and determine if the result is true or false. They are commonly used to join relational statements and make decisions. 

# and
# or
# not

# Example: Logical Operators (AND, OR, NOT) with generic variables
a, b, c = True, False, True

# AND: Both conditions must be True
if a and c:
    print("Both a and c are True (AND condition).")

# OR: At least one condition must be True
if b or c:
    print("Either b or c is True (OR condition).")

# NOT: Reverses the condition
if not b:
    print("b is False (NOT condition).")
#------------------------------------------------------------------------------------------

