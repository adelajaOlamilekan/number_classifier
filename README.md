# Overview

The Number Classifier backend is a RESTful API that classifies numbers based on predefined categories. It is built using FastAPI and provides endpoints for classifying numbers and retrieving classification results.

# Live Link
[Number Classifier API DOCS](https://number-classifier-cw4p.onrender.com/docs)

# Features

a. Gives the following data about a number:
1. number: // the number 
2. is_prime: // True or False
3. is_perfect: // True or False
4. properties: // These are the possible values["armstrong", "odd", "even"],
5. digit_sum: // sum of its digits
6. fun_fact: // Fun fact about the number; provided by [numbersapi](http://numbersapi.com/#42)

b. Asynchronous request handling with FastAPI

c. Integrated logging and error handling

# Technologies Used

1. Python (3.9+)

2. FastAPI - For building the API

3. Pydantic - For request validation

4. Uvicorn - ASGI server for running FastAPI

5. Request - For calling external API

# Installation

Ensure you have the following installed:

1. Python 3.9+

3. pip (Python package manager)

4. Docker (optional, for containerized deployment)

# Clone the Repository
```
git clone https://github.com/adelajaOlamilekan/number_classifier.git
cd number_classifier/backend
```

# Install Dependencies

Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

# Running the Application

Start the FastAPI server:

`uvicorn main:app --reload`

The API will be available at: `http://127.0.0.1:8000`

# API Endpoints

1. Classify a valid number `GET /api/classify-number?number=400`

Response:

```
{
    "number": 400,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["even"],
    "digit_sum": 4,
    "fun_fact": "400 is the number of years in a period of the Gregorian calendar, of which 97 are leap years and 303 are common."
}
```

2. Classify an invalid number `GET /api/classify-number?number=aadafaffa12233`

Response:

```
{
    "number": "alphabet",
    "error": true
}
```
# Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.

# License

This project is licensed under the MIT License. See LICENSE for details.

# Author

[Adelaja Olamilekan](https://github.com/adelajaOlamilekan)
