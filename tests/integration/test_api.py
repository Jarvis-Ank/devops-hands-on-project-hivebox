""" tests/integration/test_api.py """
import requests

# The base URL for the running container
BASE_URL = "http://localhost:8000"

def test_version_endpoint():
    """Tests if the /version endpoint returns the correct version."""
    response = requests.get(f"{BASE_URL}/version", timeout=15)

    # Check that the request was successful (status code 200)
    assert response.status_code == 200

    # Check that the response body contains the version string
    assert "0.0.1" in response.text

def test_temperature_endpoint():
    """Tests the /temperature endpoint."""
    response = requests.get(f"{BASE_URL}/temperature", timeout=15)

    # First, check that we don't get a 500 error!
    assert response.status_code == 200

    # Check that the expected key is in the JSON response
    response_json = response.json()
    assert "average_temperature" in response_json
