# Sadid Ethun
# SoftDev
# K19 -- A RESTful Journey Skyward/Restful API/Creating a flask app using a NASA API. 
# 2021-11-23
# time spent: 0.5 

from flask import Flask
from flask import render_template
import requests

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def image():
    r = requests.get("https://api.nasa.gov/planetary/apod?api_key=CpxWFgxsaXpvNJ0ReQFhG7LpydiwYW569yQljz9p")
    url = r.json()["url"]
    ex = r.json()["explanation"]
    print(url)
    return render_template("main.html", image=url, explanation=ex)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()