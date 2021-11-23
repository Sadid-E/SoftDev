from flask import Flask
import requests

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def nasa():
    r = requests.get("https://api.nasa.gov/planetary/apod?api_key=CpxWFgxsaXpvNJ0ReQFhG7LpydiwYW569yQljz9p")
    print(r.json())
    return(r.json()["url"])

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()