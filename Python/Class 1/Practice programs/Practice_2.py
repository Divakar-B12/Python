# Install an external module and use it to perform an operation of your interest. 

# pip install pyttsx 

import pyttsx3
engine = pyttsx3.init()
engine.say("My Name is Divakar")
engine.runAndWait()
