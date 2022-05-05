from flask import Flask
from flask import request
from flask import render_template
import pandas as pd
import json
import pickle

app = Flask(__name__)

model = pickle.load(open("./models/random_forest.sav", "rb"))
cities_df = pd.read_csv("./data/be.csv")

# add routes for the form, make a prediction template where we have the result and a back button
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("documentation.html", title="Home", cities=list(cities_df.city))

    if request.method == "POST":
        #try except => return expected format at fail give details 
        data = json.loads(request.data)
        predictable_data = {'Number of bedrooms': data["data"]["Bedrooms"],
                            'Living area': data["data"]["Living area"],
                            'Kitchen': data["data"]["Kitchen"],
                            'Furnished': data["data"]["Furnished"],
                            'Open fireplace': data["data"]["Fireplace"],
                            'Terrace': data["data"]["Terrace"],
                            'Garden': data["data"]["Garden"],
                            'Surface area land': data["data"]["Land area"],
                            'Pool': data["data"]["Pool"],
                            'Condition': data["data"]["Condition"],
                            'longitude': cities_df[cities_df["city"] == data["data"]["City"]].longitude,
                            'latitude': cities_df[cities_df["city"] == data["data"]["City"]].latitude,
                            'Property subtype_APARTMENT_BLOCK': 0,
                            'Property subtype_BUNGALOW': 0,
                            'Property subtype_CASTLE': 0,
                            'Property subtype_CHALET': 0,
                            'Property subtype_COUNTRY_COTTAGE': 0,
                            'Property subtype_EXCEPTIONAL_PROPERTY': 0,
                            'Property subtype_FARMHOUSE': 0,
                            'Property subtype_HOUSE': 0,
                            'Property subtype_MANOR_HOUSE': 0,
                            'Property subtype_MANSION': 0,
                            'Property subtype_MIXED_USE_BUILDING': 0,
                            'Property subtype_OTHER_PROPERTY': 0,
                            'Property subtype_TOWN_HOUSE': 0,
                            'Property subtype_VILLA:': 0
                           }

        predictable_data[f"Property subtype{data['data']['Property'].upper()}"] = 1

        df = pd.DataFrame([predictable_data])
        df.drop("Property", axis=1, inplace=True)
        df[f"Property_{data['data']['Property'].upper()}"] = [1]
        return data

        if len(data) != 3:
            return {
                "error": "3 fields expected (salary, bonus, taxes)",
                "request": data
            }

        try:
            return {
                "result": int(data["salary"]) +
                int(data["bonus"]) -
                
                int(data["taxes"])
            }
        except:
            return {
                "error": "expected numbers, got strings",
                "request": data
            }

@app.route("/web", methods=["GET"])
def web():
    return render_template("index.html", cities=cities_df.city)


if __name__ == "__main__":
    app.run()
