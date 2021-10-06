# ubun3: Shyne Choi, Aaron Contreras, Sadid Ethun
# SoftDev
# K10 -- Putting Little Pieces Together / Flask Occupations / Print random occupation and list of occupations on the webpage
# 2021-10-05

import csv
import random

from flask import Flask
app = Flask(__name__) #create instance of class Flask

def open_file():
    # Opens file and formats into dictionary as Job Class: Percentage

    with open('occupations.csv', newline = '') as f:
         reader = csv.reader(f)
         next(reader) #skips the first line

         occupations = {}

         for row in reader: #for each line in the file
            if row[0] != "Total":
                occupations[row[0]] = float(row[1])

    return occupations

def get_random(di):
    # Finds a random job occupation

    num = random.uniform(0, 99.8) # alternatively could have used random.random()*99.8

    for key in di:
        num -= di[key] # subtracts the percentage from the random number

        if (num <= 0):
            return key

    return -1

@app.route("/")       #assign fxn to route

def occupation_output():
    occ_file = open_file() # make list of occupations, call it occ_file

    # x is the string we'll be returning aka what will be on the link
    x = "<header><h3>ubun3: Shyne Choi, Aaron Contreras, Sadid Ethun</h3><br></header>"

    # start ul
    x += "<body style='font-family:arial;background-color:powderblue;'><b>Random Occupation: </b>" + get_random(occ_file) + "<br><br><br>" + "<b>List of Occupations:</b><ul>"

    # for each key in the list of occupations made earlier, we'll add it to x
    for key in occ_file:
        x += "<li>" + key + "</li>"

    # finish the unordered list (that's what ul stands for)
    x += "</ul></body>"

    return(x)


app.debug = True        # enable auto-reload upon code change
app.run()
