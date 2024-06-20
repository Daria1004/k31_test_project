import allure
from jsonschema import validate
from k31_test_project.schema.profile import schema_post_add_car, schema_delete_car, \
    schema_car_access_denied, schema_car_list


def test_profile_add_car(api_request, customer):
    api_request.set_token(customer.get_token())

    response = api_request.get_with_token('/v1/car', params={"user_id": customer.get_id()})

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200

    body = response.json()
    validate(body, schema_car_list)

    car_count_before = len(body['data'])

    payload = {
        "model": "фольксваген",
        "number": "о000оо000",
        "is_primary": 0
    }

    with allure.step('Send request with data'):
        response = api_request.post_with_token('/v1/car/add', params={"user_id": customer.get_id()}, json=payload)

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200

    body = response.json()
    validate(body, schema_post_add_car)

    assert body['status'] == 'ok'
    assert body['data']['id'] > 0
    assert body['data']['model'] == payload['model']
    assert body['data']['number'] == payload['number']

    new_car_id = body['data']['id']

    response = api_request.get_with_token('/v1/car', params={"user_id": customer.get_id()})

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200

    body = response.json()
    validate(body, schema_car_list)

    car_count_after = len(body['data'])
    assert car_count_before == car_count_after - 1

    car_ids = []
    for car in body['data']:
        car_ids.append(car['id'])

    assert new_car_id in car_ids


def test_profile_delete_car(api_request, customer, car_id):
    api_request.set_token(customer.get_token())

    response = api_request.delete_with_token('/v1/car/delete', params={"user_id": customer.get_id(), "id": car_id})

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200

    body = response.json()
    validate(body, schema_delete_car)

    with allure.step('Проверка статуса в ответе'):
        assert body['status'] == 'ok'

    with allure.step('Проверка наличия токена'):
        assert body['message'] == 'Авто успешно удалено'


def test_profile_cars_other_user(api_request, customer):
    api_request.set_token(customer.get_token())
    response = api_request.get_with_token('/v1/car', params={"user_id": 1})

    with allure.step('Проверка статус кода'):
        assert response.status_code == 200

    body = response.json()

    validate(body, schema_car_access_denied)
    with allure.step('Проверка статуса в ответе'):
        assert body['status'] == 'error'
    with allure.step('Проверка кода в ответе'):
        assert body['error_code'] == 'forbidden'

