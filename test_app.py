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
    """Test GET /weather endpoint returns successful response."""
    response = client.get('/weather')
    
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    
    data = json.loads(response.data)
    assert 'Weather' in data
    assert data['Weather'] == 'Sunny'


def test_get_weather_response_format(client):
    """Test GET /weather endpoint returns proper JSON format."""
    response = client.get('/weather')
    
    # Verify response is valid JSON
    try:
        data = json.loads(response.data)
    except json.JSONDecodeError:
        pytest.fail("Response is not valid JSON")
    
    # Verify response structure
    assert isinstance(data, dict)
    assert len(data) == 1
    assert 'Weather' in data


def test_get_weather_headers(client):
    """Test GET /weather endpoint returns correct headers."""
    response = client.get('/weather')
    
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    assert response.headers.get('Content-Type').startswith('application/json')


def test_get_weather_method_not_allowed(client):
    """Test that only GET method is allowed for /weather endpoint."""
    # Test POST method (should not be allowed)
    response = client.post('/weather')
    assert response.status_code == 405  # Method Not Allowed
    
    # Test PUT method (should not be allowed)
    response = client.put('/weather')
    assert response.status_code == 405  # Method Not Allowed
    
    # Test DELETE method (should not be allowed)
    response = client.delete('/weather')
    assert response.status_code == 405  # Method Not Allowed


def test_get_nonexistent_endpoint(client):
    """Test GET request to non-existent endpoint returns 404."""
    response = client.get('/nonexistent')
    assert response.status_code == 404


def test_get_weather_multiple_requests(client):
    """Test multiple GET requests to /weather endpoint for consistency."""
    responses = []
    
    # Make multiple requests
    for _ in range(5):
        response = client.get('/weather')
        responses.append(response)
    
    # Verify all responses are identical
    for response in responses:
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['Weather'] == 'Sunny'


def test_get_weather_with_query_parameters(client):
    """Test GET /weather endpoint with query parameters (should still work)."""
    response = client.get('/weather?city=London&units=metric')
    
    # Should still return the same response regardless of query params
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['Weather'] == 'Sunny'