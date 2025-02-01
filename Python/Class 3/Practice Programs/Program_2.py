# Write a program to fill in a letter template given below with name and date.

letter = '''
       Dear <|name|>
       Your are Selected!
       <|date|>
'''
print(letter.replace("<|name|>","Divakar").replace(" <|date|>","24 December"))
      