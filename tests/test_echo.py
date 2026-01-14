import requests

get_url = "https://postman-echo.com/get"
post_url = "https://postman-echo.com/post"

def test_empty_get():
    response = requests.get(get_url)
    assert response.status_code == 200
    data = response.json()
    assert data["args"] == {}

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

def test_body_post():
    body = {
        "name": "Ivan",
        "surname": "Ivanov",
    }
    response = requests.post(post_url, json=body)
    assert response.status_code == 200
    data = response.json()
    assert data["json"] == body

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