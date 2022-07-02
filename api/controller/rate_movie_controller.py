from api.controller.base_controller import BaseController
from config import BASE_URI
from config import API_KEY
from config import RATE_MOVIE
from config import AUTHENTICATION_TOKEN
from config import AUTHENTICATION_SESSION
from config import AUTH_BASE_URI
from config import GUEST_AUTHENTICATION_SESSION
from config import GUEST_SESSION_ID

from api.request import APIRequest


class RateMovieController(BaseController):
    def __init__(self):
        super().__init__()
        self.base_url = BASE_URI
        self.api_key = API_KEY
        self.request = APIRequest()
        self.endpoint = RATE_MOVIE
        self.request_url = f"{RATE_MOVIE}api_key={API_KEY}"

    def rate_movie(self, id, value):
        payload = {'value': value}
        rate_movie_url = f"{BASE_URI}/{id}{self.request_url}{GUEST_SESSION_ID}{self._get_guest_session_id()}"
        response = self.request.post(rate_movie_url, payload, headers=self.headers)
        return response

    def rate_movie_as_unauth(self, id, value):
        payload = {'value': value}
        rate_movie_anauth_url = f"{BASE_URI}/{id}{self.request_url}{GUEST_SESSION_ID}{self._get_guest_session_id()}_anauth"
        response = self.request.post(rate_movie_anauth_url, payload, headers=self.headers)
        return response

    def _get_request_token(self):
        token_url = f"{AUTH_BASE_URI}{AUTHENTICATION_TOKEN}api_key={API_KEY}"
        resp = self.request.get(token_url)
        token = resp.as_dict
        return token

    def _get_guest_session_id(self):
        guest_session_url = f"{AUTH_BASE_URI}{GUEST_AUTHENTICATION_SESSION}api_key={API_KEY}"
        response = self.request.get(guest_session_url, )
        resp_dict = response.as_dict
        return resp_dict['guest_session_id']

    def get_session_id(self):
        req_token = self._get_request_token()
        session_url = f"{AUTH_BASE_URI}{AUTHENTICATION_SESSION}api_key={API_KEY}"
        payload = {'request_token': req_token}
        response = self.request.post(session_url, payload, headers=self.headers)
        resp_dict = response.as_dict
        return resp_dict