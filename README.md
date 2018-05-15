# PizzaAPI
A dummy web API for a facilitating pizza delivery

## URL Link
https://pizzapi.herokuapp.com/

## Installation

```
Flask
Flask-RESTful
Flask-JWT
Flask-SQLAlchemy
```

## Description
Basic Pizza API

## Tools used:
1. Python 3.6.3
2. Flask, Flask-RESTful, Flask SQLAlchemy
3. SQLite
4. Heroku to host the site
5. POSTMAN to test the API

## Implementation and Running steps:
This project is implemented using Python3, Flask, POSTMAN, SQLAlchemy.
Perform following steps to get and post requests.
1. Install Postman
```
https://www.getpostman.com/
```
2. Open the link where API is hosted
```
https://pizzapi.herokuapp.com/
```
3. Open Postman and manage environment variables.
Following is an example:

![env test](https://github.com/sumitis14/PizzaAPI/blob/master/img/env1.JPG)

4. Declare endpoints to perform operation like below:

```
end points
```
![end text](https://github.com/sumitis14/PizzaAPI/raw/master/img/end.PNG)

5. Set environment variable in endpoints.
```
    {{url}} in GET/POST/DELETE/ endpoints
    {{jwt_token}} in Headers:
        a) Select Authorization
        b) JWT {{jwt_token}}
```
![set test](https://github.com/sumitis14/PizzaAPI/raw/master/img/env2.JPG)

6. For GET and Post an item:
```
Use Get endpoint:
    -- type {{url}}/item/<id>

Use Post\put endpoint
    -- type {{url}}/item/<name of string>
    -- in Body field add like below:
    {
	    "timeOpen" : 10,
	    "timeClose" : 20
    }
```
![get test](https://github.com/sumitis14/PizzaAPI/raw/master/img/GET.JPG)