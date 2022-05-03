from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

inputs = {'Location': "input",
          'Property subtype': ["HOUSE",
                               "APARTMENT_BLOCK",
                               "VILLA",
                               "MIXED_USE_BUILDING",
                               "FARMHOUSE",
                               "TOWN_HOUSE",
                               "MANSION",
                               "EXCEPTIONAL_PROPERTY",
                               "BUNGALOW",
                               "COUNTRY_COTTAGE",
                               "MANOR_HOUSE",
                               "OTHER_PROPERTY",
                               "CHALET",
                               "CASTLE"],
          'Price': 0,
          'Number of bedrooms': 0,
          'Living area': 0.0,
          'Kitchen': True,
          'Furnished': True,
          'Open fireplace': True,
          'Terrace': True,
          'Garden': True,
          'Surface area land': 0.0,
          'Pool': True,
          'Condition': ["Good", "Bad"]}

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html", title="Home", inputs=inputs)

    if request.method == "POST":
        data = request.form

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


if __name__ == "__main__":
    app.run()
