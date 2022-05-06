# Model deployment challenge using Docker and Heroku

This is an application deployed to Heroku to predict housing prices using the dataset scraped in a previous project.

The application provides both a web interface to predict your data and routes to access the api for predictions.

# Install

The required packages are stored in requirements.txt so if you want to run the app straight through Flask, this can be done with:
    
`pip install requirements.txt`
   
Alternatively yoy can access the Heroku app on https://challenge-model-deployment.herokuapp.com/
    
Or you could run the app from the Docker image, whatever suits your fancy.

# API

The API provides the following routes.

## Get the documentation

### Request

`GET /`

### Response

This should give you a fancier version of the README, you might even be there right now.

## Get the prediction json layout

### Request

`POST /`

### Response

```json
{
    "Send requests to /predict following this format": {
        "Bedrooms": "int",
        "City": "String containing a belgian city",
        "Condition": "bool",
        "Fireplace": "bool",
        "Furnished": "bool",
        "Garden": "bool",
        "Kitchen": "bool",
        "Land area": "int",
        "Living area": "int",
        "Pool": "bool",
        "Property": [
            "APARTMENT_BLOCK",
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
            "VILLA"
        ],
        "Terrace": "bool"
    }
}
```

## Go through the web portal

### Request

`GET /web/`

### Response

This should give you access to the web portal.

## Get the prediction json layout and instructions in the web portal

### Request

`GET /predict`

### Response

Webpage

## Predict price using data provided

### Request

`POST /predict`

#### Data layout

![Just look it up](/static/request_layout.png?raw=true)

### Response

```json
{
    "prediction": 234665.0
}
```
