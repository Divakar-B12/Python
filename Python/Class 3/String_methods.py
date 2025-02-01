# STRING FUNCTIONS:

# Some of the commonly used functions to perform operations on or manipulate strings are as follows. 

Name = "Divakar"

# Now when operated on this string ‘Name’, these functions do the following:

# 1. len () function – This function returns the length of the strings.

Name = "Divakar"
print(len(Name)) # Output:7

# 2. String.endswith("r") – This function_ tells whether the variable string ends with the string "r" or not. If string is "Divakar", it returns true for "r" since Divakar ends with r.

Name = "Divakar"
print(Name.endswith('r')) #Output : True

# 3. string.count("a") – counts the total number of occurrences of any character

Name = "Divakar"
print(Name.count('a')) #Output : 2

# 4. The first character Capitalize from a given string.

Name = "divakar"
Captalize = Name.capitalize()
print(Captalize)

# 5. string.find(word) – This function friends a word and returns the index of first occurrence of that word in the string.

Name = "ballcarrier"
find1 = Name.find("ll")
find2 = Name.find("rr")
print(find1, find2)


# 6. string.replace (old word, new word ) – This function replace the old word with new word in the entire string.

Name = "Divakat"
replace_String = Name.replace('t', "r")
print(replace_String)

# str.isalpha() - checks if all chars in string are alphabets 
# str.isdigit() - checks if all chars in string are digits

