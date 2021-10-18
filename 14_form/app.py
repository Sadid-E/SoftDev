# Text Box -- Sadid Ethun, Aaron Contreras, Gavin McGinley
# SoftDev
# K14 -- Form and Function / Flask Form App
# 2021-10-14

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. Can you predict which?
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests. Process results.
PROTIP: Insert your own in-line comments wherever they will help your future self and/or current teammates understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) 
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.headers ***")
    print(request.headers)
    # renders the login.html file when the user goes to the website
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) # prints the name of the file
    print("***DIAG: request obj ***")
    print(request) # prints the link and request method
    print("***DIAG: request.args ***")
    print(request.args) # prints the dictionary of usernames and submits
    print("***DIAG: request.args['username']  ***")
    print(request.args['username']) # prints the username from the dictionary
    print("***DIAG: request.headers ***")
    print(request.headers) # prints information about the host, the browser, and operating system
    # renders the response.html file after the user has submitted the form
    return render_template( 'response.html', username=request.args['username'], method=request.method ) #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
