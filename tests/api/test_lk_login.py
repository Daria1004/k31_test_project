import allure
import pytest
from allure_commons.types import Severity
from jsonschema import validate

import config
from k31_test_project.schema.auth import schema_post_auth_unsuccessful, schema_post_auth_successful


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Daria Jakuszewicz")
@allure.label("layer", "api")
@pytest.mark.api
@pytest.mark.login
@pytest.mark.positive
def test_auth_success(api_request):
    response = api_request.get('/v1/auth/login', auth=(f'7{config.user_login}', config.user_password))

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200

    body = response.json()
    validate(body, schema_post_auth_successful)

    with allure.step('Проверка статуса в ответе'):
        assert body['status'] == 'ok'

    with allure.step('Проверка наличия токена'):
        assert len(body['data']['token']) > 0


@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Daria Jakuszewicz")
@allure.label("layer", "api")
@pytest.mark.api
@pytest.mark.login
@pytest.mark.negative
def test_auth_fail(api_request):
    response = api_request.get('/v1/auth/login', auth=(f'7{config.user_login}', config.user_wrong_password))

    with allure.step('Проверка статус кода'):
        assert response.status_code == 401

    body = response.json()
    validate(body, schema_post_auth_unsuccessful)

    with allure.step('Проверка имени в ответе'):
        assert body['name'] == 'Unauthorized'

    with allure.step('Проверка сообщения об ошибке'):
        assert body['message'] == 'Your request was made with invalid credentials.'
