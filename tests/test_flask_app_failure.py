import os
import requests

def test_flask_invalid_endpoint():
    try:
        # Dynamically get the host and port from environment variables
        host = os.getenv("FLASK_HOST", "127.0.0.1")  # Default to localhost
        port = os.getenv("FLASK_PORT", "5000")       # Default to port 5000
        url = f"http://{host}:{port}/invalid"        # Non-existent endpoint

        response = requests.get(url)
        assert response.status_code == 404  # Expecting a 404 for a non-existent route
        print("Test Passed: Invalid endpoint returned a 404 as expected.")
    except Exception as e:
        print(f"Test Failed: {e}")
        raise

if __name__ == "__main__":
    test_flask_invalid_endpoint()