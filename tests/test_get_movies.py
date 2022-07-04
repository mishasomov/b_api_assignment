import allure
import pytest
from assertpy import assert_that

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.get_top_rated_movies_endpoint
def test_get_top_rated_movies(top_rated_movies_controller):
    response = top_rated_movies_controller.get_movies()
    assert_that(response.status_code).is_equal_to(200)


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.get_top_rated_movies_endpoint
def test_get_top_rated_movies_being_unauthorized(top_rated_movies_controller):
    response = top_rated_movies_controller.get_movies_unauthorized()
    assert_that(response.status_code).is_equal_to(401)
