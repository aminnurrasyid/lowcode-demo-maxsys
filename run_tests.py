#!/usr/bin/env python3
"""
Test runner script for Weather API tests.
Run this script to execute all test cases for the weather API.
"""
import subprocess
import sys


def run_tests():
    """Run the weather API tests using pytest."""
    try:
        print("🧪 Running Weather API Test Suite...")
        print("=" * 50)
        
        # Run pytest with verbose output
        result = subprocess.run([
            'python', '-m', 'pytest', 
            'test_weather_api.py', 
            '-v',
            '--tb=short'
        ], capture_output=True, text=True)
        
        # Print the output
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        # Check if tests passed
        if result.returncode == 0:
            print("✅ All tests passed successfully!")
        else:
            print("❌ Some tests failed!")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run_tests()