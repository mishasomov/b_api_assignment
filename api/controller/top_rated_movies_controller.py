from api.controller.base_controller import BaseController
from config import BASE_URI
from config import API_KEY
from config import TOP_RATED_MOVIES
from api.request import APIRequest


class TopRatedMoviesController(BaseController):
    def __init__(self):
        super().__init__()
        self.base_url = BASE_URI
        self.api_key = API_KEY
        self.request = APIRequest()
        self.endpoint = TOP_RATED_MOVIES
        self.request_url = f"{BASE_URI}{TOP_RATED_MOVIES}api_key={API_KEY}&language=en-US&page=1"

    def get_movies(self):
        response = self.request.get(self.request_url)
        #dict_resp = response.as_dict['results'][0]
        return response.as_dict