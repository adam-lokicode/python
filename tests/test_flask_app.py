import os
import requests

def test_flask_ping():
    """
    Test the root endpoint of the Flask app to ensure it is reachable and returns the correct response.
    """
    try:
        # Dynamically get the host and port from environment variables
        host = os.getenv("FLASK_HOST", "127.0.0.1")  # Default to localhost
        port = os.getenv("FLASK_PORT", "8080")       # Default to port 8080
        url = f"http://{host}:{port}"

        response = requests.get(url)
        assert response.status_code == 200
        assert response.text == "Welcome to United Airlines Backend!"
        print("Test Passed: Flask app root endpoint is reachable and returned the correct response.")
    except Exception as e:
        print(f"Test Failed for root endpoint: {e}")

def test_flask_booking():
    """
    Test the /booking endpoint of the Flask app to ensure it is reachable and returns the correct response.
    """
    try:
        # Dynamically get the host and port from environment variables
        host = os.getenv("FLASK_HOST", "127.0.0.1")  # Default to localhost
        port = os.getenv("FLASK_PORT", "8080")       # Default to port 8080
        url = f"http://{host}:{port}/booking"

        response = requests.get(url)
        assert response.status_code == 200
        assert response.json() == {"message": "Booking confirmed!", "status": "success"}
        print("Test Passed: Flask app /booking endpoint is reachable and returned the correct response.")
    except Exception as e:
        print(f"Test Failed for /booking endpoint: {e}")

if __name__ == "__main__":
    print("Running tests...")
    test_flask_ping()
    test_flask_booking()
    print("All tests completed.")
