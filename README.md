# Flask API Testing with pytest

This project contains a simple Flask API with comprehensive pytest test cases for GET methods.

## Project Structure

- `app.py` - Main Flask application with a GET `/weather` endpoint
- `test_app.py` - Pytest test cases for functional API testing
- `requirements.txt` - Python dependencies
- `pytest.ini` - Pytest configuration

## API Endpoints

- `GET /weather` - Returns weather information in JSON format

## Test Cases

The test suite includes the following functional API tests:

1. **test_get_weather_success** - Tests successful response from /weather endpoint
2. **test_get_weather_response_format** - Validates JSON response format
3. **test_get_weather_headers** - Checks HTTP headers and content type
4. **test_get_weather_method_not_allowed** - Ensures only GET method is allowed
5. **test_get_nonexistent_endpoint** - Tests 404 response for non-existent routes
6. **test_get_weather_multiple_requests** - Tests consistency across multiple requests
7. **test_get_weather_with_query_parameters** - Tests behavior with query parameters

## Running the Tests

### Install Dependencies

```bash
pip install --break-system-packages -r requirements.txt
```

### Run Tests

```bash
# Run all tests
python3 -m pytest test_app.py -v

# Run specific test
python3 -m pytest test_app.py::test_get_weather_success -v

# Run tests with coverage (if pytest-cov is installed)
python3 -m pytest test_app.py --cov=app -v
```

## Test Output

All tests should pass with output similar to:

```
============================= test session starts ==============================
test_app.py::test_get_weather_success PASSED                             [ 14%]
test_app.py::test_get_weather_response_format PASSED                     [ 28%]
test_app.py::test_get_weather_headers PASSED                             [ 42%]
test_app.py::test_get_weather_method_not_allowed PASSED                  [ 57%]
test_app.py::test_get_nonexistent_endpoint PASSED                        [ 71%]
test_app.py::test_get_weather_multiple_requests PASSED                   [ 85%]
test_app.py::test_get_weather_with_query_parameters PASSED               [100%]

============================== 7 passed in 0.10s
==============================
```