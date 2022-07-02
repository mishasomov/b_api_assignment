def test_get_top_rated_movies(top_rated_movies_controller):
    resp = top_rated_movies_controller.get_movies()
    assert resp.status_code == 200


def test_get_top_rated_movies_being_unauthorized(top_rated_movies_controller):
    resp = top_rated_movies_controller.get_movies_unauthorized()
    assert resp.status_code == 401
