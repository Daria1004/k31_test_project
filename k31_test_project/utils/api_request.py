import logging
import requests


class ApiRequest:
    base_url: str
    token: str

    def __init__(self, base_url):
        self.base_url = base_url

    @staticmethod
    def _log_response(response):
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logging.info("Request URL: " + response.request.url)
        if response.request.body:
            logging.info("Request body: " + str(response.request.body, encoding='utf-8'))
        logging.info("Request headers: " + str(response.request.headers))
        logging.info("Response status code " + str(response.status_code))
        logging.info("Response: " + response.text)

    def _auth_header(self):
        if self.token:
            return {"Authorization": f"Bearer {self.token}"}

    def set_token(self, token):
        self.token = token

    def get(self, endpoint, params=None, auth=None):
        response = requests.get(f'{self.base_url}{endpoint}', params=params, auth=auth)
        self._log_response(response)
        return response

    def get_with_token(self, endpoint, params=None):
        response = requests.get(f'{self.base_url}{endpoint}', params=params, headers=self._auth_header())
        self._log_response(response)
        return response

    def post_with_token(self, endpoint, params=None, data=None, json=None):
        response = requests.post(f'{self.base_url}{endpoint}'
                                 , params=params, data=data, json=json, headers=self._auth_header())
        self._log_response(response)
        return response

    def delete_with_token(self, endpoint, params=None):
        response = requests.delete(f'{self.base_url}{endpoint}', params=params, headers=self._auth_header())
        self._log_response(response)
        return response
