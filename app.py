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
        predictable_data = {"Send requests to /predict following this format": {
            "Living area": int,
            "Land area": int,
            "City": "String containing a belgian city",
            "Property": ["APARTMENT_BLOCK",
                         "BUNGALOW",
                         "CASTLE",
                         "CHALET",
                         "COUNTRY_COTTAGE",
                         "EXCEPTIONAL_PROPERTY",
                         "FARMHOUSE",
                         "HOUSE",
                         "MANOR_HOUSE",
                         "MANSION",
                         "MIXED_USE_BUILDING",
                         "OTHER_PROPERTY",
                         "TOWN_HOUSE",
                         "VILLA"],
            "Bedrooms": int,
            "Garden": bool,
            "Kitchen": bool,
            "Pool": bool,
            "Furnished": bool,
            "Fireplace": bool,
            "Terrace": bool,
            "Condition": bool
            }
        }

        return predictable_data


@app.route("/web", methods=["GET", "POST"])
def web():
    if request.method == "GET":
        return render_template("index.html", cities=cities_df.city)

    if request.method == "POST":
        data = request.form
        location = data.get("Location")
        property_type = data.get("Property")
        condition = data.get("Condition")
        kitchen = data.get("Kitchen")
        furnished = data.get("Furnished")
        fireplace = data.get("Fireplace")
        terrace = data.get("Terrace")
        garden = data.get("Garden")
        pool = data.get("Pool")
        land_area = data.get("landArea")
        living_area = data.get("livingArea")
        bedrooms = data.get("Bedrooms")

        predictable_data = {'Number of bedrooms': bedrooms,
                            'Living area': living_area,
                            'Kitchen': kitchen is not None,
                            'Furnished': furnished is not None,
                            'Open fireplace': fireplace is not None,
                            'Terrace': terrace is not None,
                            'Garden': garden is not None,
                            'Surface area land': land_area,
                            'Pool': pool is not None,
                            'Condition': condition is not None,
                            'longitude': cities_df[cities_df["city"] == location].lng,
                            'latitude': cities_df[cities_df["city"] == location].lat,
                            'property_subtype_APARTMENT_BLOCK': 0,
                            'property_subtype_BUNGALOW': 0,
                            'property_subtype_CASTLE': 0,
                            'property_subtype_CHALET': 0,
                            'property_subtype_COUNTRY_COTTAGE': 0,
                            'property_subtype_EXCEPTIONAL_PROPERTY': 0,
                            'property_subtype_FARMHOUSE': 0,
                            'property_subtype_HOUSE': 0,
                            'property_subtype_MANOR_HOUSE': 0,
                            'property_subtype_MANSION': 0,
                            'property_subtype_MIXED_USE_BUILDING': 0,
                            'property_subtype_OTHER_PROPERTY': 0,
                            'property_subtype_TOWN_HOUSE': 0,
                            'property_subtype_VILLA': 0
                           }

        predictable_data[property_type] = 1
        return render_template("predict.html", prediction=model.predict(predictable_data))


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "GET":
        return render_template("predict_help.html")

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
                            'longitude': cities_df[cities_df["city"] == data["data"]["City"]].lng,
                            'latitude': cities_df[cities_df["city"] == data["data"]["City"]].lat,
                            'property_subtype_APARTMENT_BLOCK': 0,
                            'property_subtype_BUNGALOW': 0,
                            'property_subtype_CASTLE': 0,
                            'property_subtype_CHALET': 0,
                            'property_subtype_COUNTRY_COTTAGE': 0,
                            'property_subtype_EXCEPTIONAL_PROPERTY': 0,
                            'property_subtype_FARMHOUSE': 0,
                            'property_subtype_HOUSE': 0,
                            'property_subtype_MANOR_HOUSE': 0,
                            'property_subtype_MANSION': 0,
                            'property_subtype_MIXED_USE_BUILDING': 0,
                            'property_subtype_OTHER_PROPERTY': 0,
                            'property_subtype_TOWN_HOUSE': 0,
                            'property_subtype_VILLA': 0
                           }

        predictable_data[f"property_subtype_{data['data']['Property'].upper()}"] = 1

        df = pd.DataFrame([predictable_data])
        prediction = model.predict(df)[0]
        return render_template("predict.html", prediction=prediction)

if __name__ == "__main__":
    app.run()
