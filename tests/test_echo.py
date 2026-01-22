import requests
import allure

get_url = "https://postman-echo.com/get"
post_url = "https://postman-echo.com/post"

@allure.title('Отправка пустого гет-запроса')
@allure.description('Проверяем, что при отправке гет-запроса без параметров сервер возвращает статус 200')
def test_empty_get():
    response = requests.get(get_url)
    assert response.status_code == 200
    data = response.json()
    assert data["args"] == {}

@allure.title('Гет-запрос с query-параметрами')
@allure.description('Проверка передачи query-параметров в гет-запросе. Сервер должен корректно принять и вернуть параметры name и surname')
def test_query_get():
    query = {
        "name": "Ivan",
        "surname": "Ivanov",
    }
    response = requests.get(get_url, params=query)
    assert response.status_code == 200
    data = response.json()
    assert data["args"]["name"] == "Ivan"
    assert data["args"]["surname"] == "Ivanov"

@allure.title('Пост-запрос с form-data')
@allure.description('Проверка отправки пост-запроса с form-data. Сервер должен вернуть переданные поля name и surname в разделе form')
def test_form_post():
    form = {
        "name": "Ivan",
        "surname": "Ivanov",
    }
    response = requests.post(post_url, data=form)
    assert response.status_code == 200
    data = response.json()
    assert data["form"]["name"] == "Ivan"
    assert data["form"]["surname"] == "Ivanov"

@allure.title('Пост-запрос с JSON-телом')
@allure.description('Проверка отправки пост-запроса с JSON-телом. Сервер должен корректно принять и вернуть JSON-данные')
def test_body_post():
    body = {
        "name": "Ivan",
        "surname": "Ivanov",
    }
    response = requests.post(post_url, json=body)
    assert response.status_code == 200
    data = response.json()
    assert data["json"] == body

@allure.title('Пост-запрос с заголовками')
@allure.description('Проверка передачи заголовков (headers) в пост-запросе. Сервер должен вернуть заголовки name и surname в ответе')
def test_headers_post():
    headers = {
        "name": "Ivan",
        "surname": "Ivanov",
    }
    response = requests.post(post_url, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["headers"]["name"] == "Ivan"
    assert data["headers"]["surname"] == "Ivanov"