#Write a python program to print the contents of a directory using the os module.
#Search online for the function which does that. 

import os

def list_directory_contents(path):
    try:
        # Get the list of all files and directories
        entries = os.listdir(path)
        print(f"Contents of '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"The path '{path}' is not a directory.")
    except PermissionError:
        print(f"Permission denied for accessing '{path}'.")

# Example usage
directory_path = '/TURBOC3'
list_directory_contents(directory_path)
