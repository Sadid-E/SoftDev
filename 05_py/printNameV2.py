# Sadid Ethun
# SoftDev
# K05 -- Better Living Through Amalgamation / Intro To Python / Refactoring code that creates lists of names using input and prints random name 
# 2021-09-27

# SUMMARY OF TRIO DISCUSSION
# We decided to use the code that I worked on with my previous trio. 
# The code didn't do anything when run in the terminal; it only worked in the shell.
# We decided to create a main function with a while loop that allows the user to choose what function to call.
# This keeps the code running and the user is able to keep adding and printing names until they want to stop.
# 
# DISCOVERIES
# When we tried to run our code in the terminal, we tried "python <filename.py>". 
# We kept getting an error and did not know what was causing it or what it meant. 
# After asking another classmate (Aryaman) he suggested that it might be using the wrong version of python.
# When we tried "python3 <filename.py>" it worked correctly. 
# 
# QUESTIONS
# What does if __name__=="__main__" mean and what does it do?
# Should we have our lists pre-made with names?
# 
# COMMENTS
# ...

import random

KREWES = {
    'pd1': [],
    'pd2': []
}

# Function that allows user to input name and period of student. 
# Adds the name to designated list for the period. 
def addToList():
    name = input("What is their name? ")
    period = int(input("What period is the student in? "))

    while period != 1 and period != 2:
        print("That is not a softdev period. Please input the information again.")
        period = int(input("What period is the student in? "))

    if period == 1:
        KREWES.get('pd1').append(name)
    else:
        KREWES.get('pd2').append(name)

    print(f"The student's name is {name} and their period is {period}.")

# Creates a list that combines the existing lists.
# Prints a random name from the combined list. 
def printName():
    all = KREWES.get('pd1') + KREWES.get('pd2')
    print (all[random.randrange(len(all))])

# Gives the user the option to add, print a random name, or exit.
# User can keep adding and printing names until they choose exit.
def main():
    while True:
        print('''
            1. Add a student
            2. Print out a random name
            3. Exit program
        ''')
        choice = input("Make a choice: ")
        if(choice != "1" and choice != "2" and choice != "3"):
            continue
        if(choice == "1"):
            addToList()
        if(choice == "2"):
            printName()
        if(choice == "3"):
            return
               
if __name__=="__main__":
    main()
