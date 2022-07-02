from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

BASE_URI = os.environ.get("BASE_URI")
API_KEY = os.environ.get("API_KEY")
AUTH_BASE_URI = BASE_URI.replace("/movie", "")
TOP_RATED_MOVIES = '/top_rated?'
RATE_MOVIE = '/rating?'
AUTHENTICATION_TOKEN = '/authentication/token/new?'
AUTHENTICATION_SESSION = '/authentication/session/new?'
GUEST_AUTHENTICATION_SESSION = '/authentication/guest_session/new?'
GUEST_SESSION_ID = "&guest_session_id="