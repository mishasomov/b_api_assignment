# API tests framework

Technologies
-------------
* [Requests](https://requests.readthedocs.io/en/latest/) - Requests is an elegant and simple HTTP library for Python, built for human beings.
* [Pipenv](https://pipenv.pypa.io/en/latest/) - Dependency Management
* [Pytest](https://docs.pytest.org/en/7.1.x/) - Test runner 
* [Allure reports](https://qameta.io/allure-report/) - Reporting 
* [Dotenv](https://github.com/theskumar/python-dotenv) - Python-dotenv reads key-value pairs from a .env file and can set them as environment variables
* [Cerberus](https://docs.python-cerberus.org/en/stable/) - Cerberus provides powerful yet simple and lightweight data validation for response Schemas
* [Assertpy](https://github.com/assertpy/assertpy) - Flexible Assertions
* [Docker](https://www.docker.com/) - for containerization

Getting Started
-------------
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
--------------
Git, Docker, Python

Installing
-------------
Clone the repo and then

`python -m pip install --upgrade pip`

`pip install pipenv`

`pipenv install`

Running the tests from command line mode
-------------------
cd to project path  
Run the command from cmd with parameters
* To run all tests -> `pytest --alluredir=allure_results`
* To filter tests by tag -> `pytest -v -m get_top_rated_movies_endpoint --alluredir=allure_results`

Starting Tests in Docker
-------------------
Docker container build and start commands look like:

To build container run:

`docker build -t pytest_runner .`

To start the run of the tests:

`docker run --rm -it --mount type=bind,source="$(pwd)",target=/api_test_framework/ pytest_runner`


Generate Allure Report from command line
-------------------
`allure serve allure-results`