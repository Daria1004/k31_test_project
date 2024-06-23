import config
import pytest

from k31_test_project.pages.api.customer import Customer
from k31_test_project.utils.api_request import ApiRequest


@pytest.fixture(scope='session')
def base_url():
    base_url = config.base_url_api
    return base_url


@pytest.fixture(scope='session')
def api_request(base_url):
    request = ApiRequest(base_url)

    yield request

@pytest.fixture(scope='session')
def customer(api_request):
    response = api_request.get('/v1/auth/login', auth=(f'7{config.user_login}', config.user_password))
    token = response.json()['data']['token']
    api_request.set_token(token)

    response = api_request.get_with_token('/v1/user')
    customer_id = response.json()['data']['id']

    customer = Customer(customer_id, token)

    yield customer


@pytest.fixture()
def car_id(api_request, customer):
    api_request.set_token(customer.get_token())

    payload = {
        "model": "фольксваген",
        "number": "о000оо000",
        "is_primary": 0
    }

    response = api_request.post_with_token('/v1/car/add', params={"user_id": customer.get_id()}, json=payload)

    yield response.json()['data']['id']

    api_request.delete_with_token('/v1/car/delete', params={"user_id": customer.get_id(), "id": car_id})
