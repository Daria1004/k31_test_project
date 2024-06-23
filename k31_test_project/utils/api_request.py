import requests
from k31_test_project.utils.utils_allure import log_response, attach_response


class ApiRequest:
    base_url: str
    token: [str, None]

    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def _auth_header(self):
        if self.token:
            return {"Authorization": f"Bearer {self.token}"}

    def set_token(self, token):
        self.token = token

    def request(self, method, endpoint, params=None, auth=None, data=None, json=None):
        headers = self._auth_header() if self.token and auth is None else None
        response = requests.request(method, f'{self.base_url}{endpoint}',
                                    params=params, data=data, json=json, headers=headers, auth=auth)
        log_response(response)
        attach_response(response)
        return response
