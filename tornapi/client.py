import time
from threading import Lock
from typing import Dict, Any

import requests

from .endpoints import UserEndpoint
from .exceptions import TornAPIError


class TornAPI:
    BASE_URL = 'https://api.torn.com/'

    def __init__(self, api_key: str, rate_limit: int = 100):
        self.api_key = api_key
        self.rate_limit = rate_limit
        self.requests_count = 0
        self.start_time = time.time()
        self.lock = Lock()

    def make_request(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        with self.lock:
            current_time = time.time()
            elapsed_time = current_time - self.start_time

            if elapsed_time > 60:
                self.start_time = current_time
                self.requests_count = 0

            if self.requests_count >= self.rate_limit:
                time_to_wait = 60 - elapsed_time
                print(f"Rate limit reached. Waiting for {time_to_wait:.2f} seconds.")
                time.sleep(time_to_wait)
                self.start_time = time.time()
                self.requests_count = 0

        self.requests_count += 1

        if params is None:
            params = {}
        params['key'] = self.api_key
        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
        if response.status_code != 200:
            raise TornAPIError(response.status_code, response.text)
        data = response.json()
        if 'error' in data:
            raise TornAPIError(data['error']['code'], data['error']['error'])
        return data

    @property
    def user(self) -> UserEndpoint:
        return UserEndpoint(self)
