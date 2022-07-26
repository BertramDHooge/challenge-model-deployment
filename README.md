<h2 align="center"> Model Deployment challenge</h2>
<p align="center"><a href="https://becode.org/">
<img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200"></a></p>
<h3 align="center"> Model deployment project at <a href="https://github.com/becodeorg"><strong>BeCode</strong></a></h3>
<h3 align="center"> Contributors: <a href="https://https://github.com/BertramDHooge"> Bertram D'Hooge</a> (Solo Project) </h3><br>

  
## The timeline of the project: 
* *28/04/2022 - 05/05/2022*

## Project flow

This is an application deployed to Heroku to predict housing prices using the dataset scraped in a previous project.

The application provides both a web interface to predict your data and routes to access the api for predictions.

## Next steps

The porject is finished, but the front end could use some tweaking.

## Objectives of the project: 
* Building a basic house price prediction app and deploying to Heroku.

## Usage:
The  app can be run locally using Flask, project requirements can be found in requirements.txt
   
Alternatively you can access the Heroku app (if it's currently online) on https://challenge-model-deployment.herokuapp.com/
    
Or you could run the app from the Docker image, whatever suits your fancy.

## Project outline:

* [x] Creating a basic house price prediction algoritm using data scraped in [this project](https://github.com/BertramDHooge/challenge-collecting-data)
* [x] Building an app to access the algoritm and its predictions
* [x] Deploying the app on Heroku using Docker or GitHub

## Dataset details:
[Dataset](https://github.com/BertramDHooge/challenge-collecting-data) contains the following columns :

 - [x] considered relevant for this project
 - [ ] not considered relevant for this project

* [x] Location; 
* [ ] Property type;
* [x] Property subtype;
* [x] Price;
* [ ] Type of sale;
* [x] Number of bedrooms;
* [x] Living area;
* [x] Kitchen; 
* [x] Furnished;
* [x] Open fireplace;
* [x] Terrace;
* [ ] Terrace orientation;
* [x] Garden;
* [ ] Garden orientation;
* [x] Surface area land; 
* [ ] Number of facades;
* [x] Pool;
* [x] Condition;

Location was expanded using Neonatim, then region was extracted and dummyfied. Condition and Kitchen were converted to booleans somewhat broadly.

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
