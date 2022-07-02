def test_movie_can_be_rated(rate_movie_controller):
    respns = rate_movie_controller.rate_movie(id='271236', value=10)
    assert respns.status_code == 201


def test_unable_to_rate_as_unauthorised(rate_movie_controller):
    respns = rate_movie_controller.rate_movie_as_unauth(id='271236', value=10)
    assert respns.status_code == 401


def test_rate_un_existent_movie(rate_movie_controller):
    respns = rate_movie_controller.rate_movie(id='999999999999', value=10)
    assert respns.status_code == 404


def test_response_401_schema(rate_movie_controller, validator, schemas):
    respns = rate_movie_controller.rate_movie_as_unauth(id='271236', value=10)
    respons_schema = respns.as_dict
    actual_validation_result = validator.validate(respons_schema, schemas.TOP_RATED_401)
    assert actual_validation_result is True