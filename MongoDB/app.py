from flask import Flask, render_template, jsonify, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/missiontoMars")

@app.route("/")
def index():
    try:
        mars_data = mongo.db.mars_data.find_one()
        return render_template('index.html', mars_data=mars_data)
    except:
        #return redirect("http://127.0.0.1:5000/ ", code=302)
        return redirect("http://localhost:5000/", code=302)

@app.route("/scrape")
def scrape():
    mars_data = mongo.db.mars_data
    mars_data_scrape = scrape_mars.scrape1()
    mars_data.update(
        {},
        mars_data_scrape,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)


