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

    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /thing/1
    Content-Length: 36

    {"id":1,"name":"Foo","status":"new"}

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

Webpage
