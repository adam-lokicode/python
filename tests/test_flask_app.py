import os
import requests

def test_flask_ping():
    try:
        # Dynamically get the host and port from environment variables
        host = os.getenv("FLASK_HOST", "127.0.0.1")  # Default to localhost
        port = os.getenv("FLASK_PORT", "8080")       # Default to port 8080
        url = f"http://{host}:{port}"

        response = requests.get(url)
        assert response.status_code == 200
        assert response.text == "Hello World!"
        print("Test Passed: Flask app is reachable and returned the correct response.")
    except Exception as e:
        print(f"Test Failed: {e}")

if __name__ == "__main__":
    test_flask_ping()