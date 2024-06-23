import requests
from k31_test_project.utils.utils_allure import log_response, attach_response


class ApiRequest:
    base_url: str
    token: str

    def __init__(self, base_url):
        self.base_url = base_url

    def _auth_header(self):
        if self.token:
            return {"Authorization": f"Bearer {self.token}"}

    def set_token(self, token):
        self.token = token

    def get(self, endpoint, params=None, auth=None):
        response = requests.get(f'{self.base_url}{endpoint}', params=params, auth=auth)
        log_response(response)
        attach_response(response)
        return response

    def get_with_token(self, endpoint, params=None):
        response = requests.get(f'{self.base_url}{endpoint}', params=params, headers=self._auth_header())
        log_response(response)
        attach_response(response)
        return response

    def post_with_token(self, endpoint, params=None, data=None, json=None):
        response = requests.post(f'{self.base_url}{endpoint}'
                                 , params=params, data=data, json=json, headers=self._auth_header())
        log_response(response)
        attach_response(response)
        return response

    def delete_with_token(self, endpoint, params=None):
        response = requests.delete(f'{self.base_url}{endpoint}', params=params, headers=self._auth_header())
        log_response(response)
        attach_response(response)
        return response
