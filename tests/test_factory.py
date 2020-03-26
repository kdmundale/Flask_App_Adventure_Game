from GetToTheShow import create_app

def test_config(client):
    assert not create_app(self).testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
