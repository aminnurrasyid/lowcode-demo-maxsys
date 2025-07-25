# Weather API Test Suite

This repository contains a simple Flask weather API with comprehensive test cases using pytest.

## API Endpoint

- **GET /weather** - Returns weather information

## Test Cases

The test suite includes 3 comprehensive test cases:

### 1. `test_get_weather_success`
- **Purpose**: Tests successful GET request to `/weather` endpoint
- **Verifies**: 
  - HTTP status code 200 (OK)
  - Response content type is JSON
  - Response contains expected data structure
  - Weather field contains "Sunny" value

### 2. `test_get_weather_method_not_allowed`
- **Purpose**: Tests that non-GET methods are properly rejected
- **Verifies**:
  - POST request to `/weather` returns HTTP status code 405 (Method Not Allowed)
  - API correctly handles method restrictions

### 3. `test_get_weather_with_query_parameters`
- **Purpose**: Tests GET request with query parameters
- **Verifies**:
  - API handles query parameters gracefully (e.g., `?city=London&units=metric`)
  - Still returns HTTP status code 200
  - Response format remains consistent
  - Current implementation ignores query parameters but maintains functionality

## Setup Instructions

1. **Create Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Option 1: Direct pytest command
```bash
pytest test_weather_api.py -v
```

### Option 2: Using the test runner script
```bash
python run_tests.py
```

## File Structure

```
.
├── app.py                 # Flask weather API
├── test_weather_api.py    # Test cases using pytest
├── requirements.txt       # Project dependencies
├── run_tests.py          # Test runner script
└── README.md             # This documentation
```

## Dependencies

- **Flask 2.3.3**: Web framework for the API
- **pytest 7.4.2**: Testing framework
- **pytest-flask 1.2.0**: Flask testing utilities

## Test Coverage

The test suite covers:
- ✅ Successful API responses
- ✅ HTTP method validation
- ✅ Query parameter handling
- ✅ JSON response format validation
- ✅ Status code verification