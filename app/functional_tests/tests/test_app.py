import pytest
import requests
import os

port = os.getenv("APP_PORT", 5000)
flask_host = os.getenv("FLASK_HOST", "127.0.0.1")
base_url = f"http://{flask_host}:{port}"


def test_rectangle_area():
    # response = client.get(f'{base_url}/area/rectangle', query_string={'length': 5, 'width': 10})
    response = requests.request("GET", f'{base_url}/area/rectangle', params={'length': 5, 'width': 10})
    json_data = response.json()
    assert json_data['area'] == 50.0


def test_square_area():
    # response = client.get(f'{base_url}/area/square', query_string={'side': 4})
    # json_data = response.get_json()
    response = requests.request("GET", f'{base_url}/area/square', params={'side': 4})
    json_data = response.json()
    assert json_data['area'] == 16.0


def test_circle_area():
    # response = client.get(f'{base_url}/area/circle', query_string={'radius': 7})
    # json_data = response.get_json()
    response = requests.request("GET", f'{base_url}/area/circle', params={'radius': 7})
    json_data = response.json()
    assert round(json_data['area'], 2) == round(3.14159 * 7 * 7, 2)