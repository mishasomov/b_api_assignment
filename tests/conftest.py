import pytest
from api.controller.rate_movie_controller import RateMovieController
from api.controller.top_rated_movies_controller import TopRatedMoviesController
from cerberus import Validator
from data.schemas import Schemas
import allure


@allure.step('Initialize RateMovieController')
@pytest.fixture
def rate_movie_controller():
    rate_movie_controller = RateMovieController()
    yield rate_movie_controller


@allure.step('Initialize TopRatedMoviesController')
@pytest.fixture
def top_rated_movies_controller():
    top_rated_movies_controller = TopRatedMoviesController()
    yield top_rated_movies_controller


@allure.step('Initialize Schemas Validator')
@pytest.fixture
def validator():
    validator = Validator()
    yield validator


@allure.step('Get Available Schemas')
@pytest.fixture
def schemas():
    yield Schemas
