
def test_rectangle_area(client):
    response = client.get('/area/rectangle', query_string={'length': 5, 'width': 10})
    json_data = response.get_json()
    assert json_data['area'] == 50.0


def test_square_area(client):
    response = client.get('/area/square', query_string={'side': 4})
    json_data = response.get_json()
    assert json_data['area'] == 16.0


def test_circle_area(client):
    response = client.get('/area/circle', query_string={'radius': 7})
    json_data = response.get_json()
    assert round(json_data['area'], 2) == round(3.14159 * 7 * 7, 2)