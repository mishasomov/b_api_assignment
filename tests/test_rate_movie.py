import allure
from assertpy import assert_that
import pytest

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.rate_movie_endpoint
def test_movie_can_be_rated(rate_movie_controller):
    response = rate_movie_controller.rate_movie(id='271236', value=10)
    assert response.status_code == 201


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.rate_movie_endpoint
def test_unable_to_rate_as_unauthorised(rate_movie_controller):
    response = rate_movie_controller.rate_movie_being_unauth(id='271236', value=10)
    assert_that(response.status_code).is_equal_to(401)


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.rate_movie_endpoint
def test_rate_un_existent_movie(rate_movie_controller):
    response = rate_movie_controller.rate_movie(id='999999999999', value=10)
    assert_that(response.status_code).is_equal_to(404)


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.rate_movie_endpoint
def test_response_401_schema(rate_movie_controller, validator, schemas):
    response = rate_movie_controller.rate_movie_being_unauth(id='271236', value=10)
    response_schema = response.as_dict
    actual_validation_result = validator.validate(response_schema, schemas.TOP_RATED_401)
    assert_that(actual_validation_result).is_true()
