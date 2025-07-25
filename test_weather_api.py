import pytest
import json
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_weather_success(client):
    """
    Test Case 1: Successful GET request to /weather endpoint
    Verifies that the API returns correct status code and expected JSON response.
    """
    response = client.get('/weather')
    
    # Assert status code is 200 (OK)
    assert response.status_code == 200
    
    # Assert response is JSON
    assert response.content_type == 'application/json'
    
    # Parse JSON response
    data = json.loads(response.data)
    
    # Assert response contains expected structure and data
    assert 'Weather' in data
    assert data['Weather'] == 'Sunny'


def test_get_weather_method_not_allowed(client):
    """
    Test Case 2: POST request to /weather endpoint (method not allowed)
    Verifies that the API correctly rejects non-GET requests.
    """
    response = client.post('/weather')
    
    # Assert status code is 405 (Method Not Allowed)
    assert response.status_code == 405


def test_get_weather_with_query_parameters(client):
    """
    Test Case 3: GET request with query parameters
    Verifies that the API handles query parameters gracefully and still returns expected response.
    """
    response = client.get('/weather?city=London&units=metric')
    
    # Assert status code is 200 (OK) - API should still work with query params
    assert response.status_code == 200
    
    # Assert response is JSON
    assert response.content_type == 'application/json'
    
    # Parse JSON response
    data = json.loads(response.data)
    
    # Assert response contains expected structure and data
    assert 'Weather' in data
    assert data['Weather'] == 'Sunny'
    
    # Note: Current implementation ignores query parameters,
    # but API should still return consistent response